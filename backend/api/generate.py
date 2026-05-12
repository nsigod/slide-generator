from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import deepseek_api, slide_generator

router = APIRouter()

class GenerateRequest(BaseModel):
    text: str
    output_format: str = "revealjs"  # revealjs or markdown

class GenerateResponse(BaseModel):
    success: bool
    content: str = ""
    message: str = ""

@router.post("/generate", response_model=GenerateResponse)
async def generate_slides(request: GenerateRequest):
    """根据文字生成幻灯片"""
    try:
        # 调用DeepSeek API分析文本结构
        analysis = await deepseek_api.analyze_text(request.text)

        # 根据输出格式生成内容
        if request.output_format == "revealjs":
            content = slide_generator.generate_revealjs(analysis)
        elif request.output_format == "markdown":
            content = slide_generator.generate_markdown(analysis)
        else:
            raise HTTPException(status_code=400, detail="不支持的输出格式")

        return GenerateResponse(success=True, content=content)
    except Exception as e:
        return GenerateResponse(success=False, message=str(e))
