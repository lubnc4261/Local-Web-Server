import http.server
import socketserver

PORT = 420
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Local Site started at Port", PORT)
    httpd.serve_forever()
