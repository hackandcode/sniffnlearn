__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

#
#
#

import pprint

from googleapiclient.discovery import build


class Search():
    """
    Searches the required books on google.

    This class implements the google search for the books on amazon online web store.
    The class will return required number of search result.
    The class will raise a error if it is unable to connect to
    the server.

    """
    def __init__(self):
        self.dv_key = "AIzaSyBy-F3yeKwZkdoogLU3doWgK9oUyx4mFIQ"
        return

    def search(self, query, max_limit=5):
        """
        Searches the required query and return the result

        :param query: the required query string.
        :param max_limit: the number of search result to be return, default is 5

        :return:
            returns the required search result.

        :raises:
            raises the error if unable to connect the google search api (customsearch).

        """
        service = build("customsearch", "v1",
                        developerKey=self.dv_key)
        query += " books"
        res = service.cse().list(q=query,
                                 cx='015974940825320028887:zqooin_a9z4',
                                 num=max_limit,
                                 ).execute()
        pprint.pprint(res)
        for value in res:
            if 'items' in value:
                for results in res[value]:
                    print results['formattedUrl']
