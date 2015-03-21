#!/usr/bin/python

__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

import webbrowser
import socket

from oauth2client.client import OAuth2WebServerFlow


s = socket.socket()
host = 'localhost'          # server name
port = 9003                 # server port

s.connect((host, port))
data = s.recv(1024)
s.close()                     # Close the socket when done

CLIENT_SECRET, CLIENT_ID = data.split()

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile'

# Redirect URI for installed apps
REDIRECT_URI = 'http://localhost:9004'

# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI, response_type='code')
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
webbrowser.open(authorize_url)
# creates server to accept code
s = socket.socket()
host = 'localhost'
port = 9004
s.bind((host, port))
s.listen(1)
c, addr = s.accept()     # Establish connection with client.
token_request = c.recv(1000)
c.close()                # Close the connection
s.close()
code = token_request[11:88]

credentials = flow.step2_exchange(code)
