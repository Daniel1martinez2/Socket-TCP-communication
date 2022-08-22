import socket
import time
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.15", 5000))
s.listen(5)

while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established!")

  msg = "Welcome to the server"
  msg = f'{len(msg):< {HEADER_SIZE}}' +  msg

  clientsocket.send(bytes(msg, "utf-8"))
  full_msg = ''
    
  while True:
    time.sleep(3)
    msg = f"The time is: {time.time()}"
    msg = f'{len(msg):< {HEADER_SIZE}}' +  msg
    clientsocket.send(bytes(msg, "utf-8"))

  # msg = s.recv(1024)
  # print(msg.decode("utf-8"))