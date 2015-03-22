#!/usr/bin/python

__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'


from oauth2client.client import OAuth2WebServerFlow

with open("g+secret.txt") as __file:
    data = __file.read()

CLIENT_SECRET, CLIENT_ID = data.split()

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/plus.profile.emails.read'

# Redirect URI for installed apps
REDIRECT_URI = 'http://localhost:9004'  # your server ip address

# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE,
                           redirect_uri=REDIRECT_URI, response_type='code')
authorize_url = flow.step1_get_authorize_url(redirect_uri="http://localhost:9010")

print authorize_url