#!/bin/bash

# Render API部署后端服务

API_KEY="rnd_xz6ZFCLGshoYWbbTozO6tyDQQD3s"
API_URL="https://api.render.com/v1/services"

# 创建Web服务
curl -X POST "$API_URL" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "web_service",
    "name": "slide-generator-api",
    "repo": "https://github.com/nsigod/slide-generator",
    "branch": "main",
    "rootDir": "backend",
    "buildCommand": "pip install -r requirements.txt",
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "envVars": [
      {
        "key": "DEEPSEEK_API_KEY",
        "value": "sk-71b8048405584dde84fc7a7fd733c123"
      }
    ]
  }' 2>&1 | python3 -m json.tool
