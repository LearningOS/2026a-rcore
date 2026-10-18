# Reconstructed Dockerfile from docker history
# Base image: Ubuntu 22.04
FROM ubuntu:22.04

# Build arguments
ARG RELEASE
ARG LAUNCHPAD_BUILD_ARCH
ARG QEMU_VERSION=7.0.0
ARG HOME=/root
ARG DEBIAN_FRONTEND=noninteractive

# Install basic tools
RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    python3 \
    wget \
    xz-utils

# Set working directory
WORKDIR /root

# Download and extract QEMU
RUN wget https://download.qemu.org/qemu-${QEMU_VERSION}.tar.xz && \
    tar xvJf qemu-${QEMU_VERSION}.tar.xz

# Install QEMU build dependencies
RUN apt-get install -y \
    autoconf automake autotools-dev curl libmpc-dev libmpfr-dev libgmp-dev \
    gawk build-essential bison flex texinfo gperf libtool patchutils bc \
    zlib1g-dev libexpat-dev git \
    ninja-build pkg-config libglib2.0-dev libpixman-1-dev libsdl2-dev

# Build and install QEMU
WORKDIR /root/qemu-7.0.0
RUN ./configure --target-list=riscv64-softmmu,riscv64-linux-user && \
    make -j$(nproc) && \
    make install

# Clean up QEMU build files
WORKDIR /root
RUN rm -rf qemu-${QEMU_VERSION} qemu-${QEMU_VERSION}.tar.xz

# Verify QEMU installation
RUN qemu-system-riscv64 --version && \
    qemu-riscv64 --version

# Set up Rust environment
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    RUST_VERSION=nightly-2024-05-02

# Install Rust
RUN set -eux; \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rustup-init; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --profile minimal --default-toolchain $RUST_VERSION; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME;

# Verify Rust installation
RUN rustup --version && \
    cargo --version && \
    rustc --version

# Install Rust components and tools for rCore development
RUN rustup default $RUST_VERSION; \
    cargo install cargo-binutils --version 0.4.0 --locked; \
    rustup target add riscv64gc-unknown-none-elf; \
    rustup component add rust-src; \
    rustup component add llvm-tools-preview; \
    rustup component add rustfmt; \
    rustup component add clippy;

# Set working directory
WORKDIR /root

# Default command
CMD ["/bin/bash"]
