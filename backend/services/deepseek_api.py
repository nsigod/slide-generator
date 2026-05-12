import os
from openai import OpenAI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    deepseek_api_key: str = "YOUR_DEEPSEEK_API_KEY"

    class Config:
        env_file = ".env"

settings = Settings()

# DeepSeek API配置（OpenAI兼容接口）
client = OpenAI(
    api_key=settings.deepseek_api_key,
    base_url="https://api.deepseek.com"
)

async def analyze_text(text: str) -> str:
    """使用DeepSeek API分析文本并生成幻灯片结构"""
    prompt = f"""
请将以下文字内容分析并转换为幻灯片结构。

要求：
1. 识别主要内容点，分成多个幻灯片页面
2. 每个幻灯片应有清晰的标题和内容
3. 保持原文的核心信息和逻辑结构
4. 使用Markdown格式输出，每个幻灯片用---分隔

内容：
{text}

请直接输出幻灯片结构，不要添加任何解释。
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个专业的幻灯片制作助手，擅长将文字内容转换为结构清晰的幻灯片。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"DeepSeek API调用失败: {str(e)}")
