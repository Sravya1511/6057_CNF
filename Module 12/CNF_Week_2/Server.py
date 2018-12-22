import socket
import threading
import re


StudentData = {}
# Studentdata[20158501] = ["What is my first vehicle first number?", 501]
# Studentdata[20158502] = ["What is my masters degree?", "MSIT"]
# Studentdata[20158503] = ["Who is my close friend?", "Sriram"]
# Studentdata[20158504] = ["When did you meet your close friend?", ]
file = open("data2.txt", "r")
for line in file:
	t = line.split("-")
	a = t[0]
	num = re.sub('[^0-9]','', a)
	StudentData[str(num)] = [t[1], t[2]]
	# print(t[2].rstrip('\n'))
# print(StudentData["20158502"])

host = '127.0.0.1'
port = 5000
s = socket.socket()
s.bind((host, port))
s.listen()
print("Server is ready!!")

def receive(c, message, rollnumber):
	while True:

		attendance = message.split(" ")
		if (attendance[0] ==  "MARK-ATTENDANCE"):
			if rollnumber in StudentData.keys():
				data = StudentData[rollnumber]
				c.send(str(data[0]).encode())
				password = c.recv(1024).decode()
				data2 = data[1].rstrip('\n')
				# print(data2)
				if(password == data2):
					status = "Attendance success"
					c.send(status.encode())
					# print("attendance success")
					break
				else:
					status = "Attendence failed"
					# print("attendance failure")
					c.send(status.encode())
					# c.send(str(data[0]).encode())
			else:
				print("ROLLNUMBER-NOTFOUND")
				break



while True:
	c, address = s.accept()
	print("Connection established"+str(address))
	rollnumber = c.recv(1024).decode()
	message = c.recv(1024).decode()
	threading.Thread(target = receive, args = (c, message, rollnumber)).start()
