from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ora = datetime.now().strftime("%H:%M:%S")
            html = f"""<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="1">
<style>
body {{
    background: #1a1a2e;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}}
h1 {{
    color: #00ff88;
    font-size: 80px;
    font-family: Arial, sans-serif;
}}
</style>
</head>
<body>
<h1>{ora}</h1>
</body>
</html>"""
            self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', int(os.environ.get('PORT', 8080))), Handler)
    print("Serverul rulează pe portul 8080")
    server.serve_forever()
