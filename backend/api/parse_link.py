from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import link_parser, deepseek_api, slide_generator

router = APIRouter()

class ParseLinkRequest(BaseModel):
    share_url: str

class ParseLinkResponse(BaseModel):
    success: bool
    content: str = ""
    message: str = ""

class GenerateFromLinkRequest(BaseModel):
    share_url: str
    output_format: str = "revealjs"

@router.post("/parse-link", response_model=ParseLinkResponse)
async def parse_link(request: ParseLinkRequest):
    """解析DeepSeek分享链接"""
    try:
        content = await link_parser.parse_deepseek_link(request.share_url)
        return ParseLinkResponse(success=True, content=content)
    except Exception as e:
        return ParseLinkResponse(success=False, message=str(e))

@router.post("/generate-from-link")
async def generate_from_link(request: GenerateFromLinkRequest):
    """从DeepSeek分享链接直接生成幻灯片"""
    try:
        # 解析链接
        content = await link_parser.parse_deepseek_link(request.share_url)

        # 分析内容
        analysis = await deepseek_api.analyze_text(content)

        # 生成幻灯片
        if request.output_format == "revealjs":
            result = slide_generator.generate_revealjs(analysis)
        elif request.output_format == "markdown":
            result = slide_generator.generate_markdown(analysis)
        else:
            raise HTTPException(status_code=400, detail="不支持的输出格式")

        return {"success": True, "content": result}
    except Exception as e:
        return {"success": False, "message": str(e)}
