#!/usr/bin/python

__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

import urllib2

from bs4 import BeautifulSoup


def mit_course(query, max_limit=2):
    """
    Given function returns the courses related to the query provided
    :param query: course name to be searched on the mit.edu
    :param max_limit: sets maximum search result to return (maximum value is 10)
    :return: returns the resulted search json file
    :raises: raise the error if max_limit is set larger than 10
    """
    if max_limit > 10:
        raise Exception("max_limit must be less than 10")

    a = query.split()
    query = "http://search.mit.edu/search?site=ocw&client=mit&getfields=*&" +\
                "output=xml_no_dtd&proxystylesheet=http%3A%2F%2Focw.mit.edu%2Fsearch%2Fgoogle-ocw" +\
                ".xsl&requiredfields=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&" +\
                "sectionlimit=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&as_dt=i&oe=" + \
                "utf-8&departmentName=web&filter=0&courseName=&q="
    for i in a:
        query += "+" + i
    query += "&btnG.x=0&btnG.y=0"
    response = urllib2.urlopen(query)
    html = response.read()
    soup = BeautifulSoup(html)
    res = soup.find_all('p')
    res = res[3:13]
    data = ""
    for i in res:
        data += str(i)
    soup = BeautifulSoup(data)
    data = '{"mit_ocw":['
    j = 1
    for i in soup.find_all('a'):
        data += '{"' + i.get_text() + '":"' + i.get('href') + '"},'
        if j == max_limit:
            break
        j += 1
    data += "]}"
    data = data.encode('ascii', errors='ignore')
    return data