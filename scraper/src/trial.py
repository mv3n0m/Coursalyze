from .heading import *

BASE_URL = sites['coursera'] +


def index(search):
    soup = head(BASE_URL, search)
    course_list = soup.findAll(
        'li', {'class': "ais-InfiniteHits-item"})

    lists = []
    for course in course_list:
        _title = course.find(class_='card-title').text
        _link = sites['coursera'].split(
            '/split')[0] + course.find('a').get('href')
        _image = course.find('img').get('src')
        _instructor = course.find(class_='partner-name').text
        _type = course.select(
            '.card-info>div:nth-child(3)')[0]
        _gradient = str(_type.get('class')).split('Bg_')[-1]
        _type_text = _type.text

        res = {
            'course-title': _title,
            'course-link': _link,
            'course-image': _image,
            'course-instructor': _instructor,
            'course-gradient': _gradient,
            'course-type': _type_text,
        }
        lists.append(res)
    return lists
