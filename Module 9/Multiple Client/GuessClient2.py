import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    username = input("Enter your name")
    guess = input("Enter your guess: ")

    while guess != 'q':

        s.send((guess).encode())
        data = s.recv(1024).decode()
        print(str(username)+": "+str(data))
        if(data == 'You guessed correct'):
            break
        guess = input("Enter your guess: ")

    s.close()

if __name__ == '__main__':
    Main()





