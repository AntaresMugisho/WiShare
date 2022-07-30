# This Python file uses the following encoding: utf-8
import random
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from netifaces import interfaces, ifaddresses, AF_INET


class Server():

    HOST = ""
    PORT = 34455

    def get_ip(self):
        addresses = [i["addr"] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{"addr": "0.0.0.0"}])]
        return "".join(addresses)

    def start_server(self):
        global httpd
        handler = SimpleHTTPRequestHandler

        try:
            httpd = TCPServer((self.HOST, self.PORT), handler)

        except OSError:
            httpd = TCPServer((self.HOST, self.PORT+1), handler)

        print(f"Server started\n"
              f"Serving on : {self.get_ip()}:{self.PORT}")

        httpd.serve_forever()


    def close_server(self):
        try:
            httpd.server_close()
            print("Server stopped")

        except NameError:
            pass


if __name__ == "__main__":
    server = Server()
    server.start_server()