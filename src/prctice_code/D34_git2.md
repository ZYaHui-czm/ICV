🎓 Git 课程 · 第2天：远程仓库 + 分支合并
1️⃣ 远程仓库 — 把代码备份到"云端"
大白话：本地仓库是你电脑上的存档，远程仓库（比如 GitHub）是把存档同步到网上——异地备份 + 多人协作 + 分享项目。

# 关联远程仓库（第一次）
git remote add origin https://github.com/你的用户名/仓库名.git

# 查看远程地址
git remote -v

# 推送本地 → 远程（上传）
git push origin main

# 拉取远程 → 本地（下载最新）
git pull origin main

2️⃣ 推送/拉取/克隆 — 三大远程操作
# ① push 推送（本地→远程）
git push origin main
# 把本地的 main 分支推送到远程 origin

# ② pull 拉取（远程→本地，并合并）
git pull origin main
# = git fetch + git merge

# ③ clone 克隆（第一次从远程拿整个项目）
git clone https://github.com/用户名/仓库名.git
# 会在本地新建一个文件夹，包含整个项目和历史

命令	方向	作用
push	本地→远程	上传
pull	远程→本地	下载+合并
clone	远程→本地	首次复制整个项目
fetch	远程→本地	只下载不合并
3️⃣ 分支 — 平行的"游戏进度"
大白话：写新功能时，不想破坏稳定的主代码 → 开一个分支（支线任务），在分支上随便折腾，完成后再合并回主线（main）。

# 查看分支
git branch                # 列出所有分支，* 表示当前分支

# 创建分支
git branch feature-login  # 创建分支（不切换）

# 切换分支
git checkout feature-login   # 旧版命令
git switch feature-login     # 新版命令（推荐）

# 创建并切换（一步到位）
git checkout -b feature-login
git switch -c feature-login

# 删除分支
git branch -d feature-login  # 已合并的分支
git branch -D feature-login  # 强制删除（没合并）

🔑 main 是主分支（正式版），feature-xxx 是功能分支（开发中）。命名规范：feature- 前缀。

4️⃣ 合并分支 — merge
# 把 feature-login 分支合并到 main
git checkout main          # 1. 先切回 main
git merge feature-login    # 2. 把 feature 合并进来

合并的两种情况：

Fast-forward（快进）：main 没变过，直接移动指针，无冲突
Three-way merge（三方合并）：两边都改了，需要合并，可能冲突
5️⃣ 解决冲突 — 最让人头疼的环节
大白话：两个人同时改了同一行 → Git 不知道听谁的 → 标出冲突让你自己决定。

# 冲突时文件里会出现：
<<<<<<< HEAD
# 你的版本（当前分支）
=======
# 别人的版本（合并进来的分支）
>>>>>>> feature-login

解决步骤：

打开冲突文件
手动选择保留哪个版本（或融合）
删除 <<<<<<<、=======、>>>>>>> 标记
git add 文件 → git commit 完成合并
6️⃣ 远程分支操作
# 推送分支到远程
git push origin feature-login
git push -u origin feature-login   # -u 记住关联，下次直接 git push

# 拉取远程的新分支
git fetch origin
git checkout -b feature-login origin/feature-login

# 查看远程分支
git branch -r

7️⃣ 完整协作工作流
# 日常开发（单人 + GitHub）
git pull origin main        # 1. 先同步最新
git checkout -b feature-x   # 2. 开功能分支
# ...写代码...
git add .                   # 3. 暂存
git commit -m "完成x功能"    # 4. 提交
git push origin feature-x   # 5. 推到远程
# 在 GitHub 上发起 Pull Request
# 审查通过后 merge 到 main

8️⃣ 今日常见坑
错误	正确	原因
直接改 main 分支	开 feature 分支再改	保护主线
忘了 git pull 就 push	先 pull 再 push	会冲突或拒绝
冲突标记没删干净	删掉 <<<<<<< 等	会报语法错误
git branch 创建后不切换	checkout -b 一步到位	想清楚在哪个分支
🔑 今日记忆口诀
push 上传 pull 下载 clone 首次拿
main 主线 feature 功能分支，写完 merge 合并
冲突标记 <<<<< 删干净，手动选择再提交
先 pull 后 push，别硬怼远程


<!-- 考核 -->


📝 Git 第2天考核 — 远程仓库 + 分支
一、名词解释（每题5分，共20分）
git push、git pull、git clone 三者区别 //作答：
为什么要用分支？main 和 feature 分支的区别 //作答：
Fast-forward 和 Three-way merge 的区别 //作答：
合并冲突时文件里的 <<<<<<< HEAD 是什么？ //作答：
二、命令判断（每题10分，共20分）
# 问题1：下面命令执行后，当前在哪个分支？feature 分支是否创建成功？
git branch feature-login
git checkout main
git branch

//作答：

# 问题2：判断——"只要 git push 成功，远程就一定是新的，不需要先 pull"

//作答：

三、命令补全（10分）
完成"创建功能分支 → 提交 → 推送到远程"：

git checkout -b feature-______    # 创建并切换功能分支
git add .
git commit -m "______"
git push -u origin feature-______   # -u 记住关联

四、场景操作（30分）
你和小李合作一个项目。你在 feature-ui 分支上写好了新界面并推送到了远程。现在要把这个分支合并到 main：


写出完整命令序列（包括切分支、合并、推送）。

五、概念辨析（20分）
概念A	概念B	区别？
git merge	git pull	//作答：
git branch -d	git branch -D	//作答：
📌 拓展内容（超出今日教学）
拓展①：git stash — 把未提交的改动暂时"藏起来"

git stash         # 保存当前未提交改动，工作区变干净
git stash list    # 查看 stash 列表
git stash pop     # 恢复最近的 stash

场景：改到一半要切分支，又不想提交半成品 → 用 stash。 请作答：git stash 和 git commit 的区别？ //作答：
git stash是将改动暂时缓存起来，git commit是提交改动到仓库二者有本质区别；
拓展②：git revert — 用新的提交来"撤销"旧的提交

git revert <commit_id>   # 生成一个反向提交

区别：reset --hard 是"回到过去删除历史"，revert 是"在上面叠加一个反操作"。 请作答：为什么多人协作时推荐 revert 而不是 reset --hard？ //作答：reset --hard是彻底回滚到某个历史版本，会导致别人的开发进度丢失(会被打)，严重影响项目进度，而revert
是反向提交相当于撤销了某个想要删除的提交，不会影响他人开发进度。