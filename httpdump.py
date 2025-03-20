from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, os

class RequestLogger(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log headers
        logging.info(f"Received GET request: {self.path}")
        logging.info("Headers:")
        for header, value in self.headers.items():
            logging.info(f"{header}: {value}")
        
        # Optionally log the body of the request if needed
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length:
            post_data = self.rfile.read(content_length)
            logging.info("Body:")
            logging.info(post_data.decode())

        # Send response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Request logged\n")

    def do_POST(self):
        # Log headers
        logging.info(f"Received POST request: {self.path}")
        logging.info("Headers:")
        for header, value in self.headers.items():
            logging.info(f"{header}: {value}")
        
        # Log the body of the request
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length:
            post_data = self.rfile.read(content_length)
            print("Body:")
            print(post_data.decode("utf-8", errors="replace"))


        # Send response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Request logged\n")

    def log_request(self, code='-', size='-'):
        print(f"\n{self.command} {self.path}\nHeaders: {self.headers}\n")


port = os.getenv('PORT', 80)
server = HTTPServer(("0.0.0.0", int(port)), RequestLogger)
print(f"Listening on port {port}... (Press Ctrl+C to Exit)")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print(" Have a nice day! :)")
