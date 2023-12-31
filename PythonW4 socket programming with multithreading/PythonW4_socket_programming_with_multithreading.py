#import socket programming library
import socket

#import thread module
from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
    while True:

        #if data recived from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            #lock released on exit
            print_lock.release()
            break

        #send back reversed string to client
        c.send(data)
        #reverse the given string from client
        #data = data {::-1}

        #send back reversed string to client
        c.send(data)

    #connection closed
    c.close()

def Main():
    host = ""

    #reverse a port on your computer
    #in our case it is 12345
    #b but it can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    #put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    #a forever loop until the client wants to exit

    while True:

        #establish a connectioon with client
        c, addr = s.accept()

        #lock acquired by client
        print_lock.acquire()
        print('connected to :', addr[0], ':', addr[1])

        #start a new thread and return its identifier

        start_new_thread(threaded, (c,))
    s.close()

if __name__ == '__main__':
    Main()
