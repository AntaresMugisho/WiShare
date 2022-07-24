import http.server
import socketserver
import os

from netifaces import interfaces, ifaddresses, AF_INET


def get_ip():
    addresses = [i['addr'] for i in ifaddresses("wlp3s0").setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    return " ".join(addresses)

HOST = get_ip()
PORT = 13201


class MyServer(http.server.SimpleHTTPRequestHandler):
    pass

handler = MyServer
myserver = socketserver.TCPServer((HOST, PORT), handler)

print(f"Serving on : {HOST}:{PORT}")
myserver.serve_forever()
