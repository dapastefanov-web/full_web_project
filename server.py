#!/usr/bin/env python
"""
Very simple HTTP server in python (Updated for Python 3.7)
Usage:
    ./dummy-web-server.py -h
    ./dummy-web-server.py -l localhost -p 8000
Send a GET request:
    curl http://localhost:8000
Send a HEAD request:
    curl -I http://localhost:8000
Send a POST request:
    curl -d "foo=bar&bin=baz" http://localhost:8000
This code is available for use under the MIT license.
----
Copyright 2021 Brad Montgomery
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.    
"""
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

def recepta(data, recepta_index):
    recepti = json.loads(data)["recipes"]
    html = ""
    recepta = recepti[recepta_index]
    # put a recipe title with it's ingrediants in an html variable as list elements
    html += f"<li><h1> { recepta["title"] } </h1><h3> ingredients: </h3><ul>"
    for image in recepta["img"]:
        html += f"<img src = '{ image }'>"
    for ingredient in recepta["ingredients"]:
        html += f"<li> { ingredient } </li>"
    html += "</ul>preparation:<ol>"
    for step in recepta["preparation"]:
        html += f"<li> { step } </li>"
    html += "</ol></li>"
    # puting the html variable in to the HTML as an unsorted list
    return f"<ul> { html } </ul>"

def recepti(data):
    recepti = json.loads(data)["recipes"]
    html = ""
    # put every recipe title html variable as list elements
    for i, recepta in enumerate(recepti):
        html += f'<a href = "/recepta/{i}"><li><h1> { recepta["title"] } </h1></li></a>'
    # puting the html variable in to the HTML as an unsorted list
    return f"<ul> { html } </ul>"

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        # self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f'<html><head><meta charset="utf-8"></head><body><h1>{self.path[1:]}</h1>{message}</body></html>'
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def get_data(self):
        f = open("sources/recipes.json",encoding='utf-8')
        data = f.read()
        f.close()
        return data
    def get_file(self,file):
        f = open(file)
        data = f.read()
        f.close()
        return data

    def do_GET(self):
        self._set_headers()
        if "/sources/" in self.path:
            self.wfile.write(self.get_file(self.path[1:]).encode("utf8"))
            return
        html="Home"
        if self.path == "/recepti":
            html = recepti(self.get_data())
        if "/recepta/" in self.path:
            recepta_index = int(self.path[9:])
            html = recepta(self.get_data(),recepta_index)

        self.wfile.write(self._html(html))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # 1. Изчисляване на дължината на тялото
        content_length = int(self.headers['Content-Length'])
        
        # 2. Четене на суровите данни
        post_data = self.rfile.read(content_length)
        
        # 3. Декодиране (например от UTF-8)
        decoded_data = post_data.decode('utf-8')
        personal_data = decoded_data.split("&")
        print(f"Получено тяло: {decoded_data}")
        for data in personal_data:
            print(data.split("=")[1])
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("Post"))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)