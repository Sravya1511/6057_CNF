import socket
import threading


def receive(s):
    while True:
        question = s.recv(1024).decode()
        print(question)
        answer = input("Type password: ")
        s.send(answer.encode())
        status = s.recv(1024).decode()
        if (status == 'Attendance success'):
        	print(status)
        	break
        else:
        	print(status)
        	print("TRY AGAIN")




host = '127.0.0.1'
port = 5000
s = socket.socket()
s.connect((host, port))
rollnumber = input("Enter rollnumber: ")
s.send(str(rollnumber).encode())
threading.Thread(target = receive, args = (s,)).start()
message = input("Type-MARK-ATTENDANCE ROLLNUMBER: ")
s.send(message.encode())



