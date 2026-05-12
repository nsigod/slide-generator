# 部署配置说明

## 前端部署（Vercel）

1. **推送代码到GitHub**
```bash
cd /Users/ouu/WorkBuddy/2026-05-12-task-3
git init
git add .
git commit -m "Initial commit"
# 在GitHub创建仓库后
git remote add origin https://github.com/你的用户名/slide-generator.git
git push -u origin main
```

2. **Vercel部署**
- 访问 [vercel.com](https://vercel.com)
- 点击 "New Project"
- 导入GitHub仓库
- 配置：
  - Framework Preset: `Vite`
  - Root Directory: `frontend`
  - Build Command: `npm run build`
  - Output Directory: `dist`
  - Environment Variables: 添加 `VITE_API_URL` = `https://你的后端域名.render.com`

3. **点击 Deploy**

## 后端部署（Render）

1. **推送代码到GitHub**（同上）

2. **Render部署**
- 访问 [render.com](https://render.com)
- 点击 "New + Web Service"
- 连接GitHub仓库
- 配置：
  - Name: `slide-generator-api`
  - Environment: `Python 3`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
  - Environment Variables: 添加 `DEEPSEEK_API_KEY` = `你的DeepSeek API密钥`

3. **点击 Create Web Service**

## 快速部署（推荐）

### 方案一：前后端分离部署（免费）
- 前端：Vercel（免费）
- 后端：Render（免费，有休眠）
- 优点：完全免费
- 缺点：后端长时间不用会休眠，首次访问较慢

### 方案二：全栈平台部署
- Railway（推荐）：前后端一起部署，每月$5免费额度
- 访问 [railway.app](https://railway.app)
- 连接GitHub仓库
- 自动检测并部署前后端

### 方案三：腾讯云（国内访问快）
- 轻量应用服务器：约￥50/月
- 优点：国内访问快，无休眠
- 需要：配置Nginx、域名备案

## 环境变量配置

### 前端（Vercel）
```
VITE_API_URL=https://你的后端域名.render.com
```

### 后端（Render）
```
DEEPSEEK_API_KEY=你的DeepSeek API密钥
```

## 部署后测试

1. 访问前端域名（如：`https://你的项目.vercel.app`）
2. 测试文字生成幻灯片
3. 测试链接解析功能

## 注意事项

1. **CORS配置**：部署后需要更新后端CORS设置，允许前端域名
2. **API密钥安全**：不要在代码中硬编码API密钥
3. **HTTPS**：Vercel和Render都自动提供HTTPS

## 我的推荐

**最简单方案**：
1. 前端部署到 **Vercel**（3分钟）
2. 后端部署到 **Render**（5分钟）
3. 总共8分钟，完全免费

需要我帮你执行哪个步骤？
