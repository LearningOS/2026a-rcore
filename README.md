# 专业阶段 - rCore-Tutorial

基于 [LearningOS 2026s rCore 课程模板](https://github.com/LearningOS/2026s-oscamp-professional-2026s-rcore-rCore-Tutorial-Code) 整理，由 [LearningOS](https://github.com/LearningOS) 统一分配学员仓库、自动评测并同步 OpenCamp。

**五项实验：每项 100 分 · 总分：500 分**

## 开始实验

1. 加入 [OpenCamp 秋冬季训练营](https://opencamp.cn/os2edu/camp/2026fall)，并绑定自己的 GitHub 账号。
2. 点击[领取作业仓库](https://github.com/LearningOS/2026a-enroll/issues/new?template=rcore.yml)，点击 **Create** 提交申请；等待机器人回复，然后接受仓库邀请。
3. 克隆分配的作业仓库，切换章节分支，完成实验代码和报告。
4. push 到 `ch3`、`ch4`、`ch5`、`ch6` 或 `ch8`，在 Actions 查看评测；通过后自动上传累计成绩。

完整操作：[学员指南](docs/STUDENT_GUIDE.md)。

## 分支与实验报告

| 分支 | 内容 | 分值 | 必须提交的报告 |
| --- | --- | ---: | --- |
| `main` | 课程入口与操作指南 | — | — |
| `ch1` | 应用程序与执行环境 | — | — |
| `ch2` | 批处理系统 | — | — |
| `ch3` | 多道程序与分时多任务 | 100 | `lab1` |
| `ch4` | 地址空间 | 100 | `lab1`、`lab2` |
| `ch5` | 进程管理 | 100 | `lab1` 至 `lab3` |
| `ch6` | 文件系统与 I/O | 100 | `lab1` 至 `lab4` |
| `ch7` | 进程间通信 | — | — |
| `ch8` | 并发与同步 | 100 | `lab1` 至 `lab5` |

报告放在 `reports/`，文件名为 `lab1.md` 或 `lab1.pdf` 等。请提交真实实验报告；后续章节仍需保留此前报告。

## 评分与同步

push 到 `ch3`、`ch4`、`ch5`、`ch6`、`ch8` 自动触发对应章节评测。官方测试全部通过、实验报告齐全且检查器成功退出，才记该章 100 分。重复通过不会重复加分，已通过章节的成绩会保留。

Actions 先执行 **Test chapter and reports**，通过后执行 **Save progress and upload score**。上传日志出现 `OpenCamp accepted the score (result=1).` 表示 OpenCamp 接口接受了成绩；再到学员成绩页面核对显示。

通过记录保存在学员作业仓库 `gh-pages` 分支的成绩文件中。

模板保留待完成的实验代码，直接运行时出现测试失败属于预期结果。`main`、`ch1`、`ch2`、`ch7` 不计分。

## 学员指南

- [学员指南](docs/STUDENT_GUIDE.md)

本仓库由 LearningOS 组织维护，保留上游源码历史，按 [GPL-3.0](LICENSE) 许可分发。
