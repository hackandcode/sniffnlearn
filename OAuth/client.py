import socket
import webbrowser

s = socket.socket()
host = 'localhost'             # server address
port = 9010
s.connect((host, port))
url = s.recv(1024)
s.close

webbrowser.open_new(url)

s = socket.socket()
host = 'localhost'
port = 9010
s.bind((host, port))
s.listen(1)
c, addr = s.accept()     # Establish connection with client.
c.send("User accepted.")
c.close()                # Close the connection
s.close()