import os
import sys
import platform
import http.server
import socketserver

def clear():

	import os
	os.system('cls')

clear()

PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

	print('LOCALHOST is ACTIVE')
	httpd.serve_forever()

clear()
