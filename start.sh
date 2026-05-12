#!/bin/bash

# 文字转幻灯片网站 - 启动脚本

echo "🚀 启动文字转幻灯片网站..."

# 启动后端
echo "📡 启动后端服务..."
cd /Users/ouu/WorkBuddy/2026-05-12-task-3/backend
source venv/bin/activate
pkill -f "uvicorn main:app" 2>/dev/null
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001 > backend.log 2>&1 &
echo "✅ 后端启动中... (http://localhost:8001)"

sleep 2

# 启动前端
echo "🎨 启动前端服务..."
cd /Users/ouu/WorkBuddy/2026-05-12-task-3/frontend
pkill -f "vite" 2>/dev/null
npm run dev > frontend.log 2>&1 &
echo "✅ 前端启动中... (http://localhost:5173 或 5174)"

sleep 3

# 获取前端实际端口
FRONTEND_PORT=$(lsof -i :5173 -i :5174 2>/dev/null | grep LISTEN | grep node | head -1 | awk '{print $9}' | cut -d':' -f2)
if [ -z "$FRONTEND_PORT" ]; then
    FRONTEND_PORT="5173 或 5174"
fi

echo ""
echo "✨ 启动完成！"
echo ""
echo "📱 访问地址："
echo "   前端：http://localhost:$FRONTEND_PORT"
echo "   后端API：http://localhost:8001"
echo ""
echo "📝 日志文件："
echo "   后端：/Users/ouu/WorkBuddy/2026-05-12-task-3/backend/backend.log"
echo "   前端：/Users/ouu/WorkBuddy/2026-05-12-task-3/frontend/frontend.log"
echo ""
echo "⚠️  请确保已配置 DeepSeek API 密钥："
echo "   /Users/ouu/WorkBuddy/2026-05-12-task-3/backend/.env"
