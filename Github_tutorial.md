# GitHub 新手使用指南

正道：想做什么的时候问ai怎么做，遇到报错交给ai

## 目录
1. [什么是GitHub](#什么是github)
2. [注册GitHub账号](#注册github账号)
3. [安装Git](#安装git)
4. [基本概念](#基本概念)
5. [创建第一个仓库](#创建第一个仓库)
6. [克隆仓库到本地](#克隆仓库到本地)
7. [基本Git操作](#基本git操作)
8. [团队协作流程](#团队协作流程)
9. [常见问题解决](#常见问题解决)
10. [实用技巧](#实用技巧)

## 什么是GitHub

GitHub是一个基于Git的代码托管平台，主要用于：
- 存储和管理代码
- 团队协作开发
- 版本控制
- 项目管理

## 注册GitHub账号

1. 访问 [github.com](https://github.com)
2. 点击 "Sign up" 按钮
3. 填写用户名、邮箱和密码
4. 验证邮箱地址
5. 完成注册

## 安装Git

### Windows用户
1. 下载Git for Windows: https://git-scm.com/download/win
2. 运行安装程序，使用默认设置
3. 安装完成后，打开命令提示符或PowerShell

### Mac用户
1. 打开终端
2. 运行命令：`xcode-select --install`
3. 或者下载Git for Mac: https://git-scm.com/download/mac

### Linux用户
```bash
# Ubuntu/Debian
sudo apt-get install git

# CentOS/RHEL
sudo yum install git
```

## 基本概念

### 仓库 (Repository)
- 一个项目的文件夹，包含所有文件和历史记录
- 可以是公开的（所有人可见）或私有的（只有团队成员可见）

### 分支 (Branch)
- 代码的不同版本
- 主分支通常叫 `main` 或 `master`
- 可以创建新分支来开发新功能

### 提交 (Commit)
- 保存代码更改的快照
- 每次提交都有描述信息

### 推送 (Push)
- 将本地更改上传到GitHub

### 拉取 (Pull)
- 从GitHub下载最新更改到本地

## 创建第一个仓库

### 在GitHub网站上创建
1. 登录GitHub
2. 点击右上角的 "+" 号，选择 "New repository"
3. 填写仓库名称（如：`CAN201-project`）
4. 选择公开或私有
5. 勾选 "Add a README file"
6. 点击 "Create repository"

### 配置Git（首次使用）
```bash
# 设置用户名和邮箱
git config --global user.name "你的姓名"
git config --global user.email "你的邮箱@example.com"
```

## 克隆仓库到本地

```bash
# 在GitHub仓库页面点击绿色的 "Code" 按钮，复制HTTPS链接
git clone https://github.com/用户名/仓库名.git
cd 仓库名
```

## 基本Git操作

### 查看状态
```bash
git status
```

### 添加文件到暂存区
```bash
# 添加单个文件
git add 文件名

# 添加所有文件
git add .

# 添加特定类型的文件
git add *.md
```

### 提交更改
```bash
git commit -m "描述你的更改"
```

### 推送到GitHub
```bash
git push origin main
```

### 拉取最新更改
```bash
git pull origin main
```

## 团队协作流程

### 1. 项目负责人设置
- 创建仓库
- 添加团队成员为协作者（Settings → Collaborators）
- 设置分支保护规则

### 2. 团队成员工作流程

#### 开始工作前
```bash
# 1. 克隆仓库（首次）
git clone https://github.com/用户名/项目名.git
cd 项目名

# 2. 拉取最新代码
git pull origin main
```

#### 日常开发流程
```bash
# 1. 创建新分支（为每个功能创建独立分支）
git checkout -b feature/功能名称

# 2. 进行开发工作
# 编辑文件...

# 3. 查看更改
git status
git diff

# 4. 添加更改
git add .

# 5. 提交更改
git commit -m "添加新功能：功能描述"

# 6. 推送分支到GitHub
git push origin feature/功能名称
```

#### 合并更改
1. 在GitHub上创建Pull Request (PR)
2. 团队成员审查代码
3. 合并到主分支

### 3. 解决冲突

当多人修改同一文件时可能产生冲突：

```bash
# 拉取时如果有冲突
git pull origin main

# 手动解决冲突后
git add .
git commit -m "解决冲突"
git push origin main
```

## 常见问题解决

### 1. 忘记提交信息
```bash
git commit --amend -m "新的提交信息"
```

### 2. 撤销更改
```bash
# 撤销工作区的更改
git checkout -- 文件名

# 撤销暂存区的更改
git reset HEAD 文件名
```

### 3. 查看历史记录
```bash
git log
git log --oneline
```

### 4. 切换分支
```bash
# 查看所有分支
git branch -a

# 切换分支
git checkout 分支名

# 创建并切换分支
git checkout -b 新分支名
```

## 实用技巧

### 1. 使用.gitignore文件
创建 `.gitignore` 文件来忽略不需要版本控制的文件：
```
# 忽略临时文件
*.tmp
*.log

# 忽略IDE文件
.vscode/
.idea/

# 忽略系统文件
.DS_Store
Thumbs.db
```

### 2. 提交信息规范
使用清晰的提交信息：
- `feat: 添加新功能`
- `fix: 修复bug`
- `docs: 更新文档`
- `style: 代码格式调整`
- `refactor: 重构代码`

### 3. 分支命名规范
- `feature/功能名称` - 新功能
- `bugfix/问题描述` - 修复bug
- `hotfix/紧急修复` - 紧急修复

### 4. 团队协作最佳实践
1. **经常同步**：每天开始工作前先 `git pull`
2. **小步提交**：频繁提交，每次提交只做一件事
3. **清晰描述**：提交信息要清楚说明做了什么
4. **及时沟通**：遇到问题及时在团队群或GitHub Issues中讨论
5. **代码审查**：重要更改要经过其他成员审查

## 项目文件结构建议

```
项目名/
├── README.md          # 项目说明
├── .gitignore         # 忽略文件配置
├── docs/              # 文档文件夹
│   ├── 需求文档.md
│   ├── 设计文档.md
│   └── 用户手册.md
├── src/               # 源代码
├── tests/             # 测试文件
├── assets/            # 资源文件
└── reports/           # 报告文件
```

## 紧急情况处理

### 如果代码搞坏了
```bash
# 回到上一个提交
git reset --hard HEAD~1

# 回到特定提交
git reset --hard 提交ID
```

### 如果忘记推送
```bash
# 查看本地提交
git log --oneline

# 推送到远程
git push origin main
```

## 学习资源

- [Git官方文档](https://git-scm.com/doc)
- [GitHub官方指南](https://guides.github.com/)
- [Pro Git书籍](https://git-scm.com/book)
- [GitHub Desktop](https://desktop.github.com/) - 图形界面工具

## 总结

GitHub团队协作的核心流程：
1. **克隆** → 2. **创建分支** → 3. **开发** → 4. **提交** → 5. **推送** → 6. **创建PR** → 7. **合并**

记住：**小步快跑，频繁同步**，这样团队协作会更顺畅！

---
*这份指南涵盖了GitHub团队协作的基础知识，建议团队成员先熟悉基本操作，然后在实际项目中练习。遇到问题不要害怕，Git有强大的撤销功能，大胆尝试！*
