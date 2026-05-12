import requests
from bs4 import BeautifulSoup

async def parse_deepseek_link(url: str) -> str:
    """解析DeepSeek分享链接，提取内容"""
    try:
        # 发送HTTP请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 尝试提取主要内容
        # 注意：这里需要根据DeepSeek实际页面结构调整选择器
        content_div = soup.find('div', class_='chat-content') or \
                    soup.find('div', class_='message-list') or \
                    soup.find('main')

        if content_div:
            # 提取所有文本内容
            text = content_div.get_text(separator='\n', strip=True)
            return text
        else:
            # 如果找不到特定结构，返回页面所有文本
            body = soup.find('body')
            if body:
                return body.get_text(separator='\n', strip=True)
            else:
                raise Exception("无法解析页面内容")

    except requests.RequestException as e:
        raise Exception(f"请求失败: {str(e)}")
    except Exception as e:
        raise Exception(f"解析失败: {str(e)}")
