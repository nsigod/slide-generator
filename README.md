# 文字转幻灯片网站

一个可以将文字或DeepSeek分享链接转换为Reveal.js幻灯片或Markdown文件的网站。

## 功能特性

- ✨ 支持粘贴文字直接生成幻灯片
- 🔗 支持解析DeepSeek分享链接
- 📄 支持输出Reveal.js HTML幻灯片
- 📝 支持输出Markdown文件
- 🎨 简洁的浅色界面设计

## 技术栈

### 前端
- React + TypeScript
- Vite
- Tailwind CSS

### 后端
- FastAPI
- Python 3.11+
- DeepSeek API (OpenAI兼容接口)
- BeautifulSoup4 (HTML解析)

## 快速开始

### 1. 克隆项目
```bash
cd /Users/ouu/WorkBuddy/2026-05-12-task-3
```

### 2. 配置后端

进入后端目录并创建环境变量文件：
```bash
cd backend
cp .env.example .env  # 或手动创建.env文件
```

编辑 `.env` 文件，填入你的DeepSeek API密钥：
```
DEEPSEEK_API_KEY=your_actual_deepseek_api_key_here
```

安装依赖并启动后端服务：
```bash
source venv/bin/activate
pip install -r requirements.txt  # 或手动安装依赖
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

后端将在 `http://localhost:8001` 运行。

### 3. 启动前端

打开新终端，进入前端目录：
```bash
cd frontend
npm install
npm run dev
```

前端将在 `http://localhost:5173` (或下一个可用端口) 运行。

## 使用方法

1. **从文字生成幻灯片**：
   - 在"文字输入"区域的文本框中粘贴你的内容
   - 选择输出格式（Reveal.js幻灯片 或 Markdown文件）
   - 点击"生成幻灯片"按钮
   - 在右侧预览区域查看结果
   - 点击"预览"或"下载"按钮

2. **从DeepSeek分享链接生成**：
   - 在"DeepSeek分享链接"输入框中粘贴链接
   - 点击"解析链接"按钮提取内容（可选）
   - 点击"直接生成"按钮生成幻灯片
   - 在右侧预览区域查看结果

## API接口

### POST /api/generate
根据文字生成幻灯片

**请求体**：
```json
{
  "text": "你的文字内容",
  "output_format": "revealjs"  // 或 "markdown"
}
```

### POST /api/parse-link
解析DeepSeek分享链接

**请求体**：
```json
{
  "share_url": "https://chat.deepseek.com/a/..."
}
```

### POST /api/generate-from-link
从DeepSeek分享链接直接生成幻灯片

**请求体**：
```json
{
  "share_url": "https://chat.deepseek.com/a/...",
  "output_format": "revealjs"  // 或 "markdown"
}
```

## 项目结构

```
.
├── backend/              # 后端FastAPI应用
│   ├── api/            # API路由
│   ├── services/       # 业务逻辑
│   ├── main.py         # 入口文件
│   └── requirements.txt
├── frontend/           # 前端React应用
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
└── README.md
```

## 注意事项

1. **DeepSeek API密钥**：请确保正确配置 `.env` 文件中的 `DEEPSEEK_API_KEY`
2. **CORS配置**：生产环境请修改后端CORS配置，限制允许的域名
3. **DeepSeek链接解析**：链接解析功能依赖于DeepSeek网页结构，可能需要根据实际页面更新选择器

## 后续优化

- [ ] 添加用户认证系统
- [ ] 支持更多幻灯片模板
- [ ] 添加实时预览功能
- [ ] 支持导出为PPTX格式
- [ ] 添加历史记录功能

## 许可证

MIT
