def generate_revealjs(content: str) -> str:
    """生成Reveal.js HTML幻灯片"""
    # 按---分隔幻灯片
    slides = content.split('---')

    # 生成幻灯片HTML
    slides_html = ""
    for slide_content in slides:
        slide_content = slide_content.strip()
        if not slide_content:
            continue

        # 简单的Markdown to HTML转换
        html_content = simple_markdown_to_html(slide_content)
        slides_html += f"            <section>{html_content}</section>\n"

    # 完整的Reveal.js HTML模板
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Slides</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css" id="theme">
    <style>
        .reveal {{
            font-size: 32px;
        }}
        .reveal h1 {{
            font-size: 2.5em;
            color: #1a73e8;
        }}
        .reveal h2 {{
            font-size: 1.8em;
            color: #202124;
        }}
        .reveal ul {{
            text-align: left;
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{slides_html}
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: true,
            transition: 'slide',
            backgroundTransition: 'fade',
        }});
    </script>
</body>
</html>"""

    return html

def generate_markdown(content: str) -> str:
    """生成Markdown格式幻灯片（Marp风格）"""
    # 如果内容已经包含---分隔符，直接返回
    if '---' in content:
        return f"---\\ntheme: default\\n---\\n\\n{content}"

    # 否则添加Marp前置元数据
    markdown = "---\ntheme: default\n---\n\n"
    markdown += content

    return markdown

def simple_markdown_to_html(markdown: str) -> str:
    """简单的Markdown to HTML转换"""
    html = markdown

    # 标题转换
    import re
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)

    # 列表转换（简单处理）
    lines = html.split('\n')
    in_list = False
    result = []

    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)

    if in_list:
        result.append('</ul>')

    return '\n'.join(result)
