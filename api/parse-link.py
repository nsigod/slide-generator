from http.server import BaseHTTPRequestHandler
import json
import urllib.request
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 读取请求体
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        body = json.loads(post_data.decode('utf-8'))
        
        url = body.get('url', '')
        
        try:
            # 尝试获取网页内容
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
                
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else '无标题'
            
            # 提取正文（简化版）
            paragraphs = soup.find_all('p')
            content = '\n'.join([p.get_text() for p in paragraphs[:10]])
            
            success = True
            message = '解析成功'
            
        except Exception as e:
            title = None
            content = None
            success = False
            message = str(e)
        
        # 返回响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'success': success,
            'title': title,
            'content': content,
            'message': message
        }
        
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
