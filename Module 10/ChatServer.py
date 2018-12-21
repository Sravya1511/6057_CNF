import socket
import threading

clients = []


def receive(c):
    while True:
        msg = c.recv(1024).decode()
        for i in clients:
            i.send(msg.encode())

host = '10.10.8.237'
port = 5000
s = socket.socket()
s.bind((host, port))
s.listen(10)
print("Server is Ready")
while True:
    c, address = s.accept()
    print("Connection established"+ str(address))
    # print("Welcome to the messenger")
    if (c not in clients):
        clients.append(c)
        threading.Thread(target = receive, args = (c,)).start()



