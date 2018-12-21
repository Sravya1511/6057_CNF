import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    number = input("Enter your number: ")
    # print("Generating random number....")
    # number = random.randint(1, 50)
    s.send((number).encode())

    guess = input("Enter your guess: ")

    while True:

        s.send((guess).encode())
        data = s.recv(1024).decode()
        print(str(data))
        if(data == 'You guessed correct'):
            break
        guess = input("Enter your guess: ")

    s.close()

if __name__ == '__main__':
    Main()





