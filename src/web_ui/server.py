import http.server
import socketserver
import json
import os
import urllib.request
import urllib.error

# 配置
PORT = 8000
# 尝试从环境变量获取 API Key，如果没有则需要用户手动填入
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-da9d300dd6814aaba1dc112e60dc8202") 
API_URL = "https://api.deepseek.com/chat/completions" # 确认 DeepSeek API 地址

class JarvisHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_message = data.get('message', '')
                
                # 调用 AI 模型
                ai_response = self.call_deepseek_api(user_message)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'reply': ai_response}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
        else:
            self.send_error(404)

    def call_deepseek_api(self, message):
        if DEEPSEEK_API_KEY == "sk-YOUR_API_KEY_HERE":
            return "⚠️ 请在 server.py 中配置您的 DeepSeek API Key，或者设置环境变量 DEEPSEEK_API_KEY。"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        # 构造请求体 (根据 DeepSeek API 文档)
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是 Jarvis，一个高效、专业的内阁首辅助手。请用简洁、专业的中文回答。支持 Markdown 格式。"},
                {"role": "user", "content": message}
            ],
            "stream": False
        }

        try:
            req = urllib.request.Request(API_URL, data=json.dumps(payload).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                # 假设返回结构符合 OpenAI 格式
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            return f"API 请求失败: {e.code} - {e.reason}"
        except Exception as e:
            return f"发生错误: {str(e)}"

if __name__ == "__main__":
    # 切换到脚本所在目录，确保能找到 index.html
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), JarvisHandler) as httpd:
        print(f"Jarvis Backend running at http://localhost:{PORT}")
        print(f"API Key Status: {'Configured' if DEEPSEEK_API_KEY != 'sk-YOUR_API_KEY_HERE' else 'Missing'}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
