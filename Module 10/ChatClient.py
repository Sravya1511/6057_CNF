import socket
import threading


def receive(s):
    while True:
        m = s.recv(1024).decode()
        print(m)


host = '10.10.8.237'
port = 5000
s = socket.socket()
s.connect((host, port))
username = input("enter user name")
threading.Thread(target = receive, args = (s,)).start()
while True:
    mess = input()
    message = username+'-->'+mess
    s.send(message.encode())



