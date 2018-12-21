import socket
import random
import threading


def guess(s):
    c, addr = s.accept()
    print("connection from :" + str(addr))
    number = random.randint(1, 50)
    print(number)
    while True:
        guess = c.recv(1024).decode()
        guess = int(guess)
        print("Guess: "+str(guess))

        if(guess == number) :
            data = 'You guessed correct'
            c.send((data).encode())
            break

        if(guess < number) :
            data = 'guess larger number'
            c.send((data).encode())


        if(guess > number) :
            data = 'guess smaller number'
            c.send((data).encode())


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    t = list()
    for i in range(0,3):
        t1 = threading.Thread(target=guess, args=(s,))
        t.append(t1)
        t[i].start()


    for i in range(0,3):
        t[i].join()

    # c.close()
    print("Connection closed")

if __name__ == '__main__':
    Main()
