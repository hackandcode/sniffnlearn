import urllib2,json

def search(query):
    result='Coursera courses \n'+coursera(query)+'Udacity courses \n'+udacity(query)
    return result

def coursera(query):
    handle=urllib2.urlopen("https://api.coursera.org/api/catalog.v1/courses?q=search&query="+query.replace(' ','+'))
    filer=open('coursera.json','w')
    filer.write(handle.read())
    filer.close()
    catalog=open('coursera.json')
    courses=json.load(catalog)['elements']
    coursera_response=''
    for i  in range(len(courses)):
        coursera_response+=courses[i]['name']+':'+'https://coursera.com/course/'+courses[i]['shortName']+'\n'
    return coursera_response

def udacity(query):
    catalog=open('udacity.json')
    courses=json.load(catalog)['courses']
    udacity_response=''
    for i in range(len(courses)):
        if query.lower() in courses[i]['title'].lower():
            udacity_response+=courses[i]['title']+':'+courses[i]['homepage']+'\n'
    return udacity_response
