from .heading import *

BASE_URL = sites['pluralsight'] + "/search?q={}&categories=course"


def index(search):
    soup = head(BASE_URL, search)
    course_list = soup.find('div', {'id': "search-results-category-target"})
    return soup
