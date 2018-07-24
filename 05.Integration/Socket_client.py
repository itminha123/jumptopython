import socket

# --*-- coding: utf-8 --*--
# -*- coding: utf-8 -*-

def Main():
    host = '192.168.56.1'
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" -> ")
    first_receive = True
    while message != 'q':
        mySocket.send(message.encode())
        # data = mySocket.recv(1024).decode()
        data = mySocket.recv(1024)

        if first_receive == True:
            purified_data= str(data)[2:].split('\\xff')[0]
            first_receive = False
        else:
            purified_data = str(data)[2:].split('\'')[0]


        print('Received from server: ' + str(data))
        # purified_data= str(data)[2:].split('\\xff')[0]
        print('정제된 데이타'+purified_data)
        # print('Received from server: ' + data)

        message = input(" -> ")

    mySocket.close()


if __name__ == '__main__':
    Main()