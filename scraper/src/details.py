
def head(soup, url):
    if url.split('.')[1] == "coursera":
        banner = soup.find(class_="Banner")
        d = {
            'title': banner.find('h1').text,
            'tagline': banner.find(class_="BannerTitle").find('p').text,
            'starts': soup.find(class_="BannerEnroll"),
            'enrolled': soup.find(class_="rc-ProductMetrics").text,
            'description': soup.find(class_="about-section").text,
            'provider': banner.find('img').get('src'),
            'link': url,

        }
    print(d)
    return d
