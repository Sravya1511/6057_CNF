import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("connection from :" + str(addr))
    number = c.recv(1024).decode()

    while True:
        guess = c.recv(1024).decode()
        print("Guess: "+str(guess))

        if(guess == number) :
            data = 'You guessed correct'
            c.send((data).encode())
            break

        elif(guess < number) :
            data = 'You number is greater than guess, guess larger number'
            c.send((data).encode())


        elif(guess > number) :
            data = 'You number is less than guess, guess smaller number'
            c.send((data).encode())


    c.close()
    print("Connection closed")

if __name__ == '__main__':
    Main()



