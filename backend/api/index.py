from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="文字转幻灯片API")

# CORS配置 - 允许所有来源（Vercel 部署需要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class GenerateRequest(BaseModel):
    text: str
    format: str = "revealjs"

class ParseLinkRequest(BaseModel):
    url: str

class GenerateResponse(BaseModel):
    success: bool
    content: str
    format: str
    message: Optional[str] = None

class ParseLinkResponse(BaseModel):
    success: bool
    title: Optional[str] = None
    content: Optional[str] = None
    message: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "文字转幻灯片API服务正在运行"}

@app.post("/api/generate", response_model=GenerateResponse)
async def generate_slides(request: GenerateRequest):
    """生成幻灯片"""
    try:
        # 这里简化处理逻辑
        # 实际应该调用 DeepSeek API
        
        # 临时返回示例内容
        if request.format == "revealjs":
            content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Generated Slides</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/theme/white.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section>
                <h1>示例幻灯片</h1>
                <p>这是自动生成的内容</p>
            </section>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/reveal.js"></script>
    <script>
        Reveal.initialize();
    </script>
</body>
</html>"""
        else:
            content = "# 示例幻灯片\n\n这是自动生成的内容"
        
        return GenerateResponse(
            success=True,
            content=content,
            format=request.format,
            message="生成成功"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/parse-link", response_model=ParseLinkResponse)
async def parse_link(request: ParseLinkRequest):
    """解析分享链接"""
    try:
        # 简化版：直接返回 URL 作为内容
        return ParseLinkResponse(
            success=True,
            title="解析的内容",
            content=f"来自 {request.url} 的内容",
            message="解析成功"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
