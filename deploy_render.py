#!/usr/bin/env python3
import requests
import json

API_KEY = "rnd_xz6ZFCLGshoYWbbTozO6tyDQQD3s"

# 服务配置
service_config = {
    "type": "web_service",
    "name": "slide-generator-api",
    "ownerId": "tea-d81car3bc2fs738slil0",
    "repo": "https://github.com/nsigod/slide-generator",
    "branch": "main",
    "rootDir": "backend",
    "runtime": "python",
    "serviceDetails": {
        "buildCommand": "pip install -r requirements.txt",
        "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT"
    },
    "envVars": [
        {
            "key": "DEEPSEEK_API_KEY",
            "value": "sk-71b8048405584dde84fc7a7fd733c123"
        }
    ]
}

# 发送请求
url = "https://api.render.com/v1/services"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=service_config)

# 打印结果
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
