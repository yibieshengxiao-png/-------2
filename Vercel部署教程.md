# 「冠之今天吃什么」Vercel 部署教程（自己动手版）

> 目标：把你的食谱项目部署到 Vercel，获得一个永久链接，写进简历。
> 全程你自己操作，遇到问题随时问我。

---

## 前置检查（已完成 ✅）
- [x] Git 已安装（2.55）
- [x] 项目已配置 vercel.json（Vercel 部署文件，我帮你建好了）
- [x] 图标已压缩（165MB → 11.6MB，避免部署失败）
- [x] requirements.txt（flask 依赖，已有）

---

## 第 1 步：注册 GitHub 账号（约 5 分钟）

1. 浏览器打开 https://github.com
2. 点 **Sign up**（注册）
3. 填邮箱 → 设密码 → 起用户名（建议用拼音或英文，比如 `guanzhi2026`）
4. 按提示验证邮箱（去邮箱点确认链接）
5. 完成

> 如果已经有 GitHub 账号，直接登录跳过这步。

---

## 第 2 步：把项目代码上传到 GitHub（约 10 分钟）

打开你的项目文件夹，在地址栏输入 `cmd` 回车（打开命令行），然后逐条粘贴执行：

```cmd
cd D:\冠之今天吃什么
```

先初始化仓库并提交代码：

```cmd
git init
git add .
git commit -m "冠之今天吃什么 v1.0"
```

> 如果提示 `git config user.email` 错误，先执行：
> ```cmd
> git config --global user.email "你的邮箱@xxx.com"
> git config --global user.name "你的用户名"
> ```
> 然后重新 `git commit -m "冠之今天吃什么 v1.0"`

然后在 GitHub 网站上：
1. 右上角 **+** → **New repository**（新建仓库）
2. Repository name 填：`recipe-app`（或任意名字）
3. 选 **Public**（公开，这样 Vercel 能读，别人也能看，简历展示需要）
4. 不要勾选任何初始化选项（README 等都不勾）
5. 点 **Create repository**
6. 创建后页面会显示几行命令，找到类似 `git remote add origin https://github.com/你的用户名/recipe-app.git` 的那行，**复制它**

回到命令行（cmd），粘贴执行（换成你自己的链接）：

```cmd
git remote add origin https://github.com/你的用户名/recipe-app.git
git branch -M main
git push -u origin main
```

> 第一次 push 会弹窗让你登录 GitHub（选浏览器登录），登录后自动继续。
> 看到 `main -> main` 或 `done` 字样就成功了。

---

## 第 3 步：注册 Vercel 并用 GitHub 登录（约 5 分钟）

1. 浏览器打开 https://vercel.com
2. 点 **Sign Up** → 选 **Continue with GitHub**
3. 如果没登录 GitHub 会先跳去登录，登录后回到 Vercel
4. 授权 Vercel 访问你的 GitHub（点 Authorize / 同意）
5. 完成注册，进入 Vercel 控制台（Dashboard）

---

## 第 4 步：导入项目并部署（约 5 分钟）

1. 在 Vercel Dashboard 点 **Add New...** → **Project**
2. 它会列出你的 GitHub 仓库，找到 `recipe-app`，点 **Import**
3. 进入配置页：
   - **Framework Preset**：选 **Other**（不用选 Flask，Vercel 会自动识别 Python）
   - 其他全部保持默认
4. 点 **Deploy**（部署）
5. 等待 1~3 分钟，看到 **Congratulations / Success** 就成功了

---

## 第 5 步：拿到你的链接

1. 部署成功后，页面顶部会显示你的链接，类似：
   `https://recipe-app-xxxx.vercel.app`
2. 点开链接，能正常打开你的食谱应用 = 部署成功 ✅
3. 把链接复制下来，**写进简历**

---

## 常见问题

**Q1：部署失败/报错？**
- 把报错信息截图给我，我帮你看。常见原因是 icons 没压缩或 vercel.json 有问题。

**Q2：链接打不开？**
- 国内访问 vercel.app 偶尔慢，多刷新几次；手机浏览器打不开就换电脑试试。

**Q3：以后改了代码怎么更新？**
- 重新执行 `git add .` → `git commit -m "更新说明"` → `git push`，Vercel 会自动重新部署，链接不变。

**Q4：图片显示不出来？**
- 检查 `D:\冠之今天吃什么\icons` 文件夹里的图是不是压缩版（11.6MB 那个），原图备份在 `icons_full`。

---

## 部署文件清单（都已就绪）

| 文件 | 用途 | 状态 |
|------|------|------|
| `app.py` | Flask 主程序 | ✅ 已有 |
| `requirements.txt` | Python 依赖 | ✅ 已有 |
| `vercel.json` | Vercel 配置 | ✅ 已建 |
| `templates/index.html` | 前端页面 | ✅ 已有 |
| `data_*.py` | 数据 | ✅ 已有 |
| `icons/` | 压缩版图标 11.6MB | ✅ 已准备 |
