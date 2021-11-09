import http.server
import socketserver
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("192.168.8.2", PORT), Handler) as httpd:
    print("serving at port", PORT)
    # if(httpd.verify_request(request=))
    httpd.serve_forever()

