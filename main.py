import socket
import socketserver
import logging
import time
import sys

import sipfullproxy
from sipfullproxy import UDPHandler

HOST, PORT = '0.0.0.0', 5060
# HOST, PORT = '192.168.1.17', 5060

print("Hello worldus")

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO, datefmt='%H:%M:%S')
logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
hostname = socket.gethostname()
logging.info(hostname)
ipaddress = socket.gethostbyname(hostname)
# if ipaddress == "127.0.0.1":
# ipaddress = sys.argv[1]
# ipaddress = "192.168.1.17"
logging.info(ipaddress)

sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)

server = socketserver.UDPServer((HOST, PORT), UDPHandler)
server.serve_forever()


