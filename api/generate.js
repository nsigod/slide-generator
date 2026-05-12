export default function handler(req, res) {
  // 只处理 POST 请求
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { text, format = 'revealjs' } = req.body;
    
    // 生成幻灯片内容
    let content = '';
    
    if (format === 'revealjs') {
      content = `<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Generated Slides</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/theme/white.css">
    <style>
        .reveal h1 { font-size: 2.5em; }
        .reveal p { font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section>
                <h1>生成的幻灯片</h1>
                <p>${text.substring(0, 200)}...</p>
            </section>
            <section>
                <h2>内容详情</h2>
                <p>${text}</p>
            </section>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.0/dist/reveal.js"></script>
    <script>
        Reveal.initialize({
            hash: true,
            slideNumber: true
        });
    </script>
</body>
</html>`;
    } else {
      // Markdown 格式
      content = `# 生成的幻灯片\n\n${text}`;
    }
    
    return res.status(200).json({
      success: true,
      content: content,
      format: format,
      message: '生成成功'
    });
    
  } catch (error) {
    return res.status(500).json({
      success: false,
      content: '',
      format: req.body.format || 'revealjs',
      message: error.message
    });
  }
}
