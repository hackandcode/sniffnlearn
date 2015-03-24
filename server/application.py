import json,requesto
def main():
    query=raw_input("Enter Query:")
    result=requesto.requester(query)
    jsonner=open("results.json","w")
    jsonner.write(result)
    jsonner.close()
    myfile=open("results.json")
    print "lol"
    JsonObj=json.load(myfile)
    displayResults(JsonObj)
    rating=input("\nPlease rate the search to exit(1-5):")
    
def displayResults(JsonObj):
    print 
    print "Coursera Results :\n"
    for i in range(5):
        print "Title:"+(JsonObj['coursera'][i]).keys()
        print '->'+(JsonObj['coursera'][i]).values()

    print "Udacity Results :\n"
    for i in range(5):
        print "Title:"+JsonObj['Udacity'][i]['title']
        print '->'+JsonObj['Udacity'][i]['link']

    print "Books Results :\n"
    for i in range(5):
        print "Title:"+JsonObj['Books'][i]['title']
        print '->'+JsonObj['Books'][i]['link']
    return

if __name__=='__main__':
    main()
