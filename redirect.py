#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('HTTP request received:')
        peticion = recvSocket.recv(1024)
        print (peticion)
        aleat = str(random.randint(1, 10000000))
        recvSocket.send(bytes("HTTP/1.1 301 \r\n\r\n" + "<html><meta http-equiv='Refresh'" +
                "content=3;url=" + "http://localhost:1234/" + aleat +
                "><body><p>Redirigiendo a... " + "http://localhost:1234/" + aleat +
                "</p></body></html>", "utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    print ("Closing binded socket")
mySocket.close()
