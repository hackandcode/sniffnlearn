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
    url = "http://search.mit.edu/search?site=ocw&client=mit&getfields=*&" +\
                "output=xml_no_dtd&proxystylesheet=http%3A%2F%2Focw.mit.edu%2Fsearch%2Fgoogle-ocw" +\
                ".xsl&requiredfields=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&" +\
                "sectionlimit=WT%252Ecg_s%3ACourse+Home|WT%252Ecg_s%3AResource+Home&as_dt=i&oe=" + \
                "utf-8&departmentName=web&filter=0&courseName=&q="
    url += query
    url += "&btnG.x=0&btnG.y=0"
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    res = soup.find_all('p')
    res = res[3:max_limit+3]
    data = ""
    for i in res:
        data += str(i)
    soup = BeautifulSoup(data)
    data = '{"mit_ocw":['

    for i in soup.find_all('a'):
        data += '{"' + i.get_text() + '":"' + i.get('href') + '"},'

    data += "]}"
    data = data.encode('ascii', errors='ignore')
    return data
