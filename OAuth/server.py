from socket import *
import thread
import subprocess
 
BUFF = 1024
HOST = 'localhost'      # must be input parameter @TODO
PORT = 9003             # must be input parameter @TODO


def handler(client_sock):
    while 1:
        data = subprocess.check_output(["python", "g+client_auth.py"])
        data.trim()
        client_sock.send(data)
        client_sock.close()
 
if __name__ == '__main__':
    ADDR = (HOST, PORT)
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_sock.bind(ADDR)
    server_sock.listen(5)
    while 1:
        __client_sock, addr = server_sock.accept()

        thread.start_new_thread(handler, __client_sock)