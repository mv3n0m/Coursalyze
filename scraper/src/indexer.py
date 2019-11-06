import requests

from bs4 import BeautifulSoup
from requests.compat import quote_plus
from urllib.request import Request, urlopen
from . import courses, details


sites = {
    'coursera': "https://www.coursera.org/search?query={}",
    # 'udemy': "https://www.udemy.com",
    'futurelearn': "https://www.futurelearn.com/search?filter_type=course&q={}",
    # 'trial': "https://www.pluralsight.com",
}

headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64; rv: 69.0) Gecko/20100101 Firefox/69.0",
}

final_list = []


def index(search, filters):
    course_source = filters.get('source')
    course_type = filters.get('course-type')
    provider = filters.get('provider')
    final_list.clear()
    for key, value in sites.items():
        response = requests.get(value.format(search), headers=headers)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        course_list = courses.head(key, soup)

        for list_item in course_list:
            list_item['src'] = value.split('/search')[0]
            final_list.append(list_item)
            if course_source or course_type or provider:
                print(course_source, course_type, provider)
                if course_source and list_item['src'].split('.')[1] not in course_source and list_item in final_list:
                    final_list.remove(list_item)
                if course_type and list_item['course_type'].lower() not in course_type and list_item in final_list:
                    final_list.remove(list_item)
                if provider and list_item['course_provider'].lower() not in provider and list_item in final_list:
                    final_list.remove(list_item)

    return final_list


def detail(slug):
    for items in final_list:
        if items.get('course_title') == slug:
            url = items.get('src') + items.get('course_link')
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, features='html.parser')
            data = details.head(soup, url)
    return data
