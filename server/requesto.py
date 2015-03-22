import requests

def requester(query):
    a=requests.get("http://localhost:8002/"+query.replace(' ','+'))
    return str(a.text)
