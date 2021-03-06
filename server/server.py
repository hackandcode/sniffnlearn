from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import searcher
import socket

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message =searcher.search(parsed_path.query)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8002), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
