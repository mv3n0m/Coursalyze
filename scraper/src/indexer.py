import requests

from bs4 import BeautifulSoup
from requests.compat import quote_plus
from urllib.request import Request, urlopen
from . import courses


sites = {
    'coursera': "https://www.coursera.org/search?query={}",
    # 'udemy': "https://www.udemy.com",
    'futurelearn': "https://www.futurelearn.com/search?filter_type=course&q={}",
    # 'trial': "https://www.pluralsight.com",
}

headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64; rv: 69.0) Gecko/20100101 Firefox/69.0",
}


def index(search):
    final_list = []
    for key, value in sites.items():
        response = requests.get(value.format(search), headers=headers)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        course_list = courses.head(key, soup)

        for list_item in course_list:
            list_item['src'] = value.split('/search')[0]
            final_list.append(list_item)

    return final_list
