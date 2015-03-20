__author__ = 'amit.gupta.ece13@iitbhu.ac.in (DarKnight)'

#
#
#

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
        self.book_query = ""
        self.paper_query = ""
        self.book_index = 1
        self.paper_index = 1
        return

    def __search(self, query, index, max_limit=5):
        """
        Searches the required query and return the result

        :param query: the required query string.
        :param max_limit: the number of search result to be return, default is 5

        :return:
            returns the JSON file of required search result.

        :raises:
            raises the error if unable to connect the google search api (customsearch).

        """
        service = build("customsearch", "v1",
                        developerKey=self.dv_key)
        res = service.cse().list(q=query,
                                 cx='015974940825320028887:zqooin_a9z4',
                                 num=max_limit,
                                 start=index,
                                 ).execute()
        return res

    def search_book(self, query, max_limit=5):
        """
        Provides the books search result on amazon site as per the query
        :param query: Topic to search
        :param max_limit: Maximum number of search result to be shown
        :return: returns the JSON file of required search result.
        """
        query += " books"
        self.book_query = query
        return self.__search(self.book_query, max_limit=max_limit, index=self.book_index)

    def search_paper(self, query, max_limit=5):
        """
        Provides the research paper search result as per the query
        :param query: Topic to search
        :param max_limit:  Maximum number of search result to be shown
        :return: returns the JSON file of required search result.
        """
        query = "filetype:pdf ' " + query + "' research paper"
        self.paper_query = query
        return self.__search(self.paper_query, max_limit=max_limit, index=self.paper_index)

    def search_next(self, default=0):
        """
        Provides the next search result from google search api
        :param default: If set to 0 research paper search result
                        is returned else books search result is returned
        :return: returns the JSON file of required search result.
        """
        if default:
            self.book_index += 5
            return self.__search(self.book_query, index=self.book_index)
        else:
            self.paper_index += 5
            return self.__search(self.paper_index, index=self.paper_index)