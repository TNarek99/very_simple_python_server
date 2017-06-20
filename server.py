# from socket import *
#
# def createServer():
#     serversocket = socket(AF_INET, SOCK_STREAM)
#     serversocket.bind(('localhost',9000))
#     serversocket.listen(5)
#     while(1):
#         (clientsocket, address) = serversocket.accept()
#         clientsocket.send("It works")
#
# createServer()

import SimpleHTTPServer
import SocketServer

PORT = 3000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "server listening on port : ", PORT
httpd.serve_forever()
