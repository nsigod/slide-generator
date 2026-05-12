from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# 创建 FastAPI 应用
app = FastAPI()

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class ParseLinkRequest(BaseModel):
    url: str

@app.post("/api/parse-link")
async def parse_link(request: ParseLinkRequest):
    """解析分享链接"""
    try:
        # 简化版：直接返回 URL 作为内容
        return {
            "success": True,
            "title": "解析的内容",
            "content": f"来自 {request.url} 的内容",
            "message": "解析成功"
        }
    except Exception as e:
        return {
            "success": False,
            "title": None,
            "content": None,
            "message": str(e)
        }

@app.get("/")
async def root():
    return {"message": "Parse Link API is running"}
