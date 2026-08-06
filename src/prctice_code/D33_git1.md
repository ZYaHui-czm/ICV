# Git基础
🎓 Git 课程 · 第1天：核心概念 + 本地操作
1️⃣ Git 是什么？
大白话：Git 是一个时光机 + 存档系统。你写的每个版本都能存下来，随时可以回到任意一个历史版本，还能多个人一起写同一个项目不打架。

类比：写文档时的"另存为 v1、v2、v3"——但 Git 自动帮你做，还支持分支、合并、回滚。

2️⃣ 三个概念必须先懂
概念	大白话	类比
仓库 (Repository)	被 Git 管理的文件夹	一个"存档游戏"
提交 (Commit)	一次"存档"	游戏里按保存键
分支 (Branch)	平行的"游戏进度"	主线+支线任务
3️⃣ 工作区 → 暂存区 → 仓库（最核心！）
这是 Git 最重要的一张图，务必记牢：

工作区（Working Directory）    →    暂存区（Staging Area）    →    仓库（Repository）
你正在编辑的文件                        git add 后的文件               git commit 后的文件

# ① 修改文件 → 文件在"工作区"
# ② git add → 文件进入"暂存区"（准备提交）
git add file.txt
git add .              # 添加所有改动

# ③ git commit → 文件进入"仓库"（正式存档）
git commit -m "这次改了什么"

🔑 理解重点：add 是"挑好要存档的东西"，commit 是"正式按下存档键"。add 可以多次，commit 一次打包。

4️⃣ 初始化仓库
# 在项目文件夹里运行
git init          # 初始化：让这个文件夹变成 Git 仓库

# 查看当前状态（最常用的命令！）
git status        # 显示哪些文件改了、哪些没提交

git status 会告诉你三种状态：

Untracked files — 新文件还没被 Git 跟踪
Changes not staged — 改了但还没 add
Changes to be committed — 已 add 待 commit
5️⃣ 配置身份（第一次必须做）
# 告诉 Git 你是谁（提交记录上会显示）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 查看配置
git config --global --list

6️⃣ 查看历史
git log                # 查看提交历史
git log --oneline      # 简洁版（每个提交一行）
git log --oneline --graph  # 带分支图

7️⃣ 回滚 / 撤销
# 工作区的修改不要了（还没 add）
git checkout -- file.txt      # 丢弃 file.txt 的修改
git restore file.txt          # 新版命令（推荐）

# 已 add 想撤销暂存（还没 commit）
git reset HEAD file.txt       # 取消暂存

# 撤销最后一次 commit（保留改动）
git reset --soft HEAD~1       # 回到上一个提交，改动保留在暂存区

# 彻底回到某个历史版本
git reset --hard <commit_id>  # ⚠️ 危险！会丢弃之后的改动

⚠️ reset --hard 会永久删除改动，用之前先确认！

8️⃣ 忽略文件 — .gitignore
大白话：有些文件不该进仓库——比如密钥、缓存、虚拟环境、临时文件。

# .gitignore 文件内容
venv/               # 忽略整个文件夹
__pycache__/        # 忽略缓存
*.pyc               # 忽略所有 .pyc
.env                # 密钥文件绝不提交！
secret.txt

git add .gitignore  # 把 .gitignore 本身提交，规则才生效

9️⃣ 完整工作流（记住这个循环）
# 一次正常的开发循环
git status              # 1. 看看改了啥
git add .               # 2. 挑选改动
git commit -m "描述"    # 3. 存档
git log --oneline       # 4. 查看历史

🔑 今日记忆口诀
工作区改文件，add 进暂存，commit 落仓库
git status 常看，git log 看历史
.gitignore 排除敏感文件
reset --hard 要谨慎，改动会消失


==================

<!-- 考核 -->

📝 Git 课程 · 第1天考核 — 核心概念 + 本地操作
一、名词解释（每题5分，共20分）
工作区、暂存区、仓库三者的关系 //作答：
git add 和 git commit 各自的作用 //作答：
git status 会显示哪三种状态？ //作答：
.gitignore 是干什么的？ //作答：
二、命令判断（每题10分，共20分）
# 问题1：下面命令的执行结果是什么？
git init
echo "hello" > test.txt
git add test.txt
git commit -m "第一次提交"
echo "world" >> test.txt
git status

//作答：最后 git status 会显示什么？

# 问题2：判断对错——"git reset --hard 是安全的，可以放心使用"

//作答：

三、命令补全（10分）
把文件加入暂存并提交：

git ______ file.txt    # 加入暂存区
git ______ -m "提交信息"   # 正式提交

四、场景操作（30分）
你改了 3 个文件（a.py、b.py、c.py），但只想提交其中 a.py 和 b.py，c.py 留到下次再提交。写出完整命令序列。
如果已经add：git reset HEAD c.py
git commit -m "提交信息"；如果没有add：git add a.py
git add b.py
git commit -m "提交信息"

五、概念辨析（20分）
概念A	概念B	区别？
git commit	直接复制文件夹备份	//作答：
git reset --soft	git reset --hard	//作答：

📌 拓展内容（本次考核新增，超出今天教学）
拓展：git diff — 查看文件具体改了什么（今天只教了 status/log 查"有没有改"，diff 查"具体改了哪些行"）

git diff              # 工作区 vs 暂存区的差异
git diff --staged     # 暂存区 vs 仓库的差异

请作答：git diff 和 git status 的区别是什么？ //作答：diff是看改的内容，status是看状态。