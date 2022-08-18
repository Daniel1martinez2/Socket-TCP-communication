import socketserver
from sqlite3 import connect
import time
import threading
import socket

# class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass
# class MyTCPRequestHandler(socketserver.StreamRequestHandler):
#     # handle() method will be called once per connection
#     num = 0
#     def handle(self):      
#       addr = self.request.getpeername()
#       print(f"{addr} connected")
#       msg = self.rfile.readline().strip()
#       print("Data Recieved from client is:".format(msg), msg)
#       MyTCPRequestHandler.num += 1
#       self.wfile.write(f"Hello Client {MyTCPRequestHandler.num}".encode())
          
# aServer = MyServer(("192.168.0.15", 8080), MyTCPRequestHandler)
# print(f"Started: {aServer}")
# # Listen for ever
# aServer.serve_forever()

import socket 
import threading

HEADER = 64
PORT = 8080
SERVER = "172.30.78.75" 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()