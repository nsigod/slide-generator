from http.server import BaseHTTPRequestHandler
import json
import os

def handler(request):
    """Vercel Serverless Function for generating slides"""
    
    # 只处理 POST 请求
    if request.method == "POST":
        try:
            # 读取请求体
            body = json.loads(request.body)
            text = body.get("text", "")
            format = body.get("format", "revealjs")
            
            # 生成幻灯片内容（简化版）
            if format == "revealjs":
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
                <h1>生成的幻灯片</h1>
                <p>文本内容：""" + text[:100] + """...</p>
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
                content = "# 生成的幻灯片\n\n" + text
            
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "success": True,
                    "content": content,
                    "format": format,
                    "message": "生成成功"
                })
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "success": False,
                    "content": "",
                    "format": format if 'format' in locals() else "revealjs",
                    "message": str(e)
                })
            }
    else:
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Method not allowed"})
        }
