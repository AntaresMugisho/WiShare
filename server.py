# This Python file uses the following encoding: utf-8
import random
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from netifaces import interfaces, ifaddresses, AF_INET
class Server:

    HOST = ""
    PORT = 13201

    def get_ip(self):
        addresses = [i["addr"] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{"addr": "0.0.0.0"}])]
        return "".join(addresses)

    def start_server(self):
        handler = SimpleHTTPRequestHandler
        server = TCPServer((self.HOST, self.PORT), handler)

        print("Server started")
        print(f"Serving on : {self.get_ip()}:{self.PORT}")
        server.serve_forever()

    def close_server(self):
        try:
            self.close_server()
            print("Server stopped")

        except Exception as e:
            print("Unable to stop server")
            print("ERR.SV.26:", e)

    def essai(self):
        a = random.randint(12, 20)
        print(a)
        if a == 12:
            return 'Antares'

if __name__ == "__main__":
    server = Server()
    server.start_server()