# This Python file uses the following encoding: utf-8

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from netifaces import interfaces, ifaddresses, AF_INET



class Server:

    HOST = ""
    PORT = 13201

    def get_ip(self):
        addresses = [i["addr"] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{"addr": "0.0.0.0"}])]
        return "".join(addresses)

    def launch_server(self):
        handler = SimpleHTTPRequestHandler
        server = TCPServer((self.HOST, self.PORT), handler)

        print(f"Serving on : {self.get_ip()}:{self.PORT}")
        server.serve_forever()

        server.server_close()
        print("Server stopped")

    def close_server(self):
        print("Closing ...")

if __name__ == "__main__":
    server = Server()
    server.launch_server()