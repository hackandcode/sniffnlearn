import urllib2,json,pprint

def search(query):
    catalog=open('udacity.json')
    courses=json.load(catalog)['courses']
    response=''
    for i in range(len(courses)):
        if query.lower() in courses[i]['title'].lower():
            response+=courses[i]['title']+':'+courses[i]['homepage']+'\n'
    return response
