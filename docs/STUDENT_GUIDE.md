# 专业阶段 - rCore-Tutorial：领取仓库到自动评测

本课程的作业仓库由 `LearningOS` 组织分配。

## 1. 绑定账号并接受邀请

加入 [OpenCamp 秋冬季训练营](https://opencamp.cn/os2edu/camp/2026fall)，并绑定自己实际使用的 GitHub 账号。

点击[领取作业仓库](https://github.com/LearningOS/2026a-enroll/issues/new?template=rcore.yml)，点击 **Create** 提交申请。系统直接读取申请人的 GitHub 登录名，不需要手填账号。等待机器人回复，打开邀请链接并接受仓库协作邀请。

分配的仓库为 `LearningOS/2026a-rcore-你的GitHub登录名`，包含 `main` 与 `ch1` 至 `ch8`。课程模板 `LearningOS/2026a-rcore` 不用于提交个人作业。

## 2. 克隆分配的仓库

本地需要 Git 和课程实验环境。下列命令使用 SSH；请先把自己的 SSH 公钥配置到 GitHub 账号，把 `YOUR_GITHUB_LOGIN` 替换成自己的登录名。

```sh
git clone git@github.com:LearningOS/2026a-rcore-YOUR_GITHUB_LOGIN.git
```

克隆分配的组织仓库，Git 使用自己的 SSH 身份认证。

```sh
cd 2026a-rcore-YOUR_GITHUB_LOGIN
```

进入刚克隆的仓库。

## 3. 完成并提交实验

```sh
git switch ch3
```

切换到第 3 章实验分支。按照 [rCore 实验指导](https://learningos.github.io/rCore-Tutorial-Guide/) 完成代码，并提交真实的 `reports/lab1.md` 或 `reports/lab1.pdf` 实验报告。

```sh
git diff
```

检查自己的源码和报告修改。

```sh
git add os reports
```

把实验代码和报告加入本次提交；需要新增其他实验文件时，把相应路径明确加入。

```sh
git commit -m "Complete rCore chapter 3"
```

保存本次修改，`-m` 指定提交说明。

```sh
git push origin ch3
```

推送到自己仓库的 `ch3` 分支，并触发该章评测。

## 4. 查看评测与成绩

进入自己仓库的 **Actions**，打开刚触发的运行。

1. **Test chapter and reports**：运行 QEMU 和官方检查器，检查测试及实验报告。只有全部测试通过、报告齐全、检查器退出状态为 0 时，该章才通过。
2. **Save progress and upload score**：记录已通过章节，将累计成绩上传到 OpenCamp。日志显示 `OpenCamp accepted the score (result=1).` 表示接口接受了成绩。
3. 返回 OpenCamp 的学员成绩页面刷新，核对自己账号与课程。接口接受成绩与网页实际显示是两个验收步骤。

运行附件包含 `rcore-grade.log` 和 `rcore-result.json`，保留 30 天。成功记录保存在自己仓库 `gh-pages` 分支的成绩文件；无需开启 GitHub Pages 网站服务。

只推送未完成的模板代码时，测试失败是正常结果，不会上传通过成绩。

## 5. 按章节继续提交

| 分支 | 该章分值 | 必须保留的实验报告 |
| --- | ---: | --- |
| `ch3` | 100 | `lab1` |
| `ch4` | 100 | `lab1`、`lab2` |
| `ch5` | 100 | `lab1`、`lab2`、`lab3` |
| `ch6` | 100 | `lab1` 至 `lab4` |
| `ch8` | 100 | `lab1` 至 `lab5` |

报告放在 `reports/` 下，使用 `.md` 或 `.pdf`。切换下一章后检查此前报告是否仍然存在；各章节分支独立，报告需要一并保留。不要为同步报告而合并整条章节分支，以免混入不同章的内核代码。

每章全部通过后记 100 分，总分 500；重复通过同一章不会重复加分。已通过章节的成绩保留，之后失败的提交不会扣除此前分数。

只有 `ch3`、`ch4`、`ch5`、`ch6`、`ch8` 的 push 自动评分；`main`、`ch1`、`ch2`、`ch7` 不评分。也可以在 Actions 中选择 **Run workflow**，并选择对应实验分支；选择 `main` 会跳过评分。

## 常见问题

| 现象 | 检查与处理 |
| --- | --- |
| push 提示没有权限 | 确认已接受仓库邀请，SSH 账号与分配的学员账号一致 |
| 缺少章节分支 | 联系维护者补齐；建仓需要复制全部分支 |
| push 后没有运行 | 检查是否推送到五个评分分支，Actions 是否启用，提交说明是否含 `[skip ci]` |
| 测试没有全部通过 | 查看 Actions 日志，修改代码或报告后重新 push |
| N/N 但任务失败 | 继续查看报告检查及检查器退出状态；N/N 本身不足以通过 |
| 上传作业被跳过 | 联系维护者核对 `STUDENT_GITHUB`；只有对应学员触发的运行上传成绩 |
| 提示课程 Secret 缺失 | 联系维护者检查课程配置 |
| `user is not join` | 加入 [OpenCamp 秋冬季训练营](https://opencamp.cn/os2edu/camp/2026fall)，并绑定分配仓库时使用的 GitHub 账号 |
| 写入 `gh-pages` 返回 403 | 联系维护者检查工作流 `contents: write` 权限及组织 Actions 策略 |
| 上传接口返回其他错误 | 保留返回错误信息，交由维护者检查课程配置 |

维护者可以运行 **Check student configuration** 检查作业仓库配置。

账号或权限修复后，可重跑原工作流。上传失败时已通过章节的记录保留，重试不会重复加分。
