const https = require('https');
const http = require('http');

module.exports = (req, res) => {
  // 只处理 POST 请求
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { url } = req.body;
    
    if (!url) {
      return res.status(400).json({
        success: false,
        message: 'URL is required'
      });
    }
    
    // 获取网页内容
    const protocol = url.startsWith('https') ? https : http;
    
    protocol.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (response) => {
      let html = '';
      
      response.on('data', (chunk) => {
        html += chunk;
      });
      
      response.on('end', () => {
        // 简单解析 HTML
        const titleMatch = html.match(/<title>(.*?)<\/title>/i);
        const title = titleMatch ? titleMatch[1] : '无标题';
        
        // 提取所有段落文本
        const paragraphs = [];
        const pRegex = /<p>(.*?)<\/p>/gi;
        let match;
        while ((match = pRegex.exec(html)) !== null) {
          const text = match[1].replace(/<[^>]*>/g, '');
          if (text.trim()) {
            paragraphs.push(text);
          }
        }
        
        const content = paragraphs.slice(0, 10).join('\n\n');
        
        return res.status(200).json({
          success: true,
          title: title,
          content: content || '无法提取内容',
          message: '解析成功'
        });
      });
      
    }).on('error', (error) => {
      return res.status(500).json({
        success: false,
        title: null,
        content: null,
        message: `解析失败: ${error.message}`
      });
    });
    
  } catch (error) {
    return res.status(500).json({
      success: false,
      title: null,
      content: null,
      message: error.message
    });
  }
};
