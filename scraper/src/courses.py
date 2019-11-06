tasks = {}


def task(f): return tasks.setdefault(f.__name__, f)


@task
def coursera(soup):
    course_list = soup.findAll(
        'li', {'class': "ais-InfiniteHits-item"})
    lists = []
    for course in course_list:
        d = {
            'course_title': course.find(class_='card-title').text,
            'course_link': course.find('a').get('href'),
            'course_image': course.find('img').get('src'),
            'course_provider': course.find(class_='partner-name').text,
            'course_type': course.select(
                '.card-info>div:nth-child(3)')[0].text,
            'course_ratings': str(course.select('.rc-Ratings>span:nth-child(2)'))[25:28],
        }
        lists.append(d)
    return lists


@task
def futurelearn(soup):
    course_list = soup.findAll('li', {'class': "m-link-list__item"})
    lists = []
    for course in course_list:
        d = {
            'course_type': course.find(class_='headline').text.upper(),
            'course_link': course.findAll('a')[0].get('href'),
            'course_title': course.find('h3').text,
            'course_provider': course.findAll('a')[1].text,
            'course_image':  # "http://amspec.ph/products/amspec/JC12.jpg",
            # "https://www.carnival.com/_ui/responsive/ccl/assets/images/notfound_placeholder.svg",
            "https://wfpl.org/wp-content/plugins/lightbox/images/No-image-found.jpg",
        }
        lists.append(d)
    return lists


def head(key, soup):
    return tasks[key](soup)
