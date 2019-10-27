from .heading import *

BASE_URL = sites['udemy'] + "/courses/search/?q={}"


def index(search):
    r = Request(BASE_URL.format(quote_plus(search)), headers=headers)
    webpage = urlopen(r).read()
    soup = BeautifulSoup(webpage, "html.parser")
    # title = soup.find("title")

    return soup
