# This Python file uses the following encoding: utf-8
import random
from http.server import SimpleHTTPRequestHandler
import http
from socketserver import TCPServer
import socketserver
from netifaces import interfaces, ifaddresses, AF_INET


def get_host():
    addresses = [i["addr"] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{"addr": "0.0.0.0"}])]
    return "".join(addresses)


HOST = get_host()
PORT = 34444
DIRECTORY = "/home"

def handler_from(directory):
    def _init(self, *args, **kwargs):
        return http.server.SimpleHTTPRequestHandler.__init__(self, *args, directory=self.directory, **kwargs)
    return type(f'HandlerFrom<{directory}>',
                (http.server.SimpleHTTPRequestHandler,),
                {'__init__': _init, 'directory': directory})

def start_server(directory):
    global httpd

    with socketserver.TCPServer((HOST, PORT), handler_from(directory)) as httpd:
        print(f"Server started\n"
              f"Serving on : {HOST}:{PORT}")
        httpd.serve_forever()

def stop_server():
    try:
        httpd.server_close()
        print("Server stopped")
    except:
        pass

if __name__ == "__main__":
    start_server(DIRECTORY)