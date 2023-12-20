import socket
import time
import random
import os

lHost = '127.0.0.1'
port = 99

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
    sckt.connect((lHost,port))
    msg = input('please insert your message to send :\n')
    sckt.sendall(bytes(msg,encoding='UTF-8'))
    # while True:
    data = sckt.recv(4068)
    data = data.decode('utf-8')

print(f'The result of {data} command is :\n')
os.system(str(data))
