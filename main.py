from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

from netifaces import interfaces, ifaddresses, AF_INET

HOST = "0.0.0.0"
PORT = 13200

def get_ip():
    addresses = [i["addr"] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{"addr":"No IP addr"}])]
    return " ".join(addresses)


def launch_server():
    handler = SimpleHTTPRequestHandler
    server = TCPServer((HOST, PORT), handler)

    print(f"Serving on : {get_ip()}:{PORT}")
    server.serve_forever()

    server.server_close()
    print("Server stopped")


if __name__ == "__main__":
    launch_server()
