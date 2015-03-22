import urllib2, json
import MySQLdb
import Search

def search(query):
    rating = 0.0
    query = query.replace('+', ' ')
    result = ''
<<<<<<< HEAD

    connection = MySQLdb.connect("localhost", "root", "sunita","code42day")#create database manually
=======
    connection = MySQLdb.connect("localhost", "root", "newpass@123","code42day")#create database manually
>>>>>>> b2c0a88cd277958036018a84d2449a947b82623e
    '''change hostname from localhost to your server IP
    change user from 'root' to your user
    change pass to your user's pass
    '''
    query1 = query
    query = query.replace(' ', '').lower()
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Searches (striptext VARCHAR(50),search TEXT,rating FLOAT)")
    d = cur.execute("SELECT * FROM Searches WHERE striptext='%s';" % (str(query))  )
    if (d):
        result = cur.fetchall()
        result = (result[0])[1]
    else:
	print "check"
        books = Search.Search()
        data_books = books.search_book(query)
        coursera_result = coursera(query1)
        udacity_result = udacity(query1.replace('+', ' '))
        result = data_books + coursera_result + udacity_result
	print "hello"
	print query
        cur.execute("INSERT INTO Searches(striptext,search,rating) \
                            VALUES('%s','%s',%f);" % (str(query),str(result),rating))
	connection.commit()
    connection.close()
    return json.dumps(result,ensure_ascii=True)


def coursera(query):
    try:
        handle = urllib2.urlopen("https://api.coursera.org/api/catalog.v1/courses?q=search&query=" + query)
    except Exception:
        return ""
    data = '{"coursera":['
    filer = open('coursera.json', 'w')
    filer.write(handle.read())
    filer.close()
    catalog = open('coursera.json')
    courses = json.load(catalog)['elements']
    for i in range(len(courses)):
        data += '{"' + courses[i]['name'] + '":"' + 'https://coursera.com/course/' + courses[i]['shortName'] + '"},'
        if i == 4:
            break
    data += "],"
    data = data.encode('ascii', errors='ignore')
    # re.sub(r'[^\x00-\x7F]','', data)
    coursera_response = data
    return coursera_response


def udacity(query):
    catalog = open('udacity.json')
    courses = json.load(catalog)['courses']
    data = '{"Udacity":['
    query = query.replace('+', ' ')
    for i in range(len(courses)):
        if query.lower() in courses[i]['title'].lower():
            data += '{"' + courses[i]['title'] + '":"' + courses[i]['homepage'] + '"}'
    data += "]}"
    data = data.encode('ascii', errors='ignore')
    udacity_response = data
    return udacity_response
