import os, sys

from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = '.'
port =8888


os.chdir(webdir)
server_addr = ("",port)
server_obj = HTTPServer(server_addr,CGIHTTPRequestHandler)
server_obj.serve_forever()