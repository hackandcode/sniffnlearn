#!/usr/bin/python

__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

import socket


with open("g+secret.txt") as file:
    data = file.read()


s = socket.socket()
host = 'localhost'
port = 9003
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()     # Establish connection with client.
    token_request = c.send(data)
    c.close()                # Close the connection