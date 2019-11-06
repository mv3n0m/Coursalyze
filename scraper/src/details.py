
def head(soup, url):
    if url.split('.')[1] == "coursera":
        banner = soup.find(class_="Banner")
        glance = soup.find(class_="ProductGlance")
        instructors = soup.find(class_="Instructors").findAll(
            class_="instructorWrapper_jfe7wu")
        l = []
        for instructor in instructors:
            instructor_sc = instructor.find(class_="caption-text"),
            instructor_t = instructor.text,
            n = instructor.find('h3').text

            if instructor_sc[0]:
                # .split('>')[1].rstrip('</div')
                sc = list(instructor_sc[0])[0]
                t = instructor_t[0].lstrip(n).rstrip(sc)
            else:
                sc = "Data not available"
                t = "Data not available"

            i = {
                'instructor_name': n,
                'instructor_img': instructor.find('img', {'class': "Avatar_7khxo7"}).get('src'),
                'instructor_title': t,
                'instructor_school': sc,
            }
            l.append(i)

        skills = soup.find(class_="Skills").findAll(
            'span', {'class': "centerContent_dqfu5r"}),
        s = []
        for skill in list(skills[0]):
            s.append(skill.text)

        d = {
            'title': banner.find('h1').text,
            'tagline': banner.find(class_="BannerTitle").find('p').text,
            # 'starts': soup.find(class_="startdate").find('span').text,
            'enrolled': soup.find(class_="rc-ProductMetrics").text.split(' ')[0],
            'description': soup.find(class_="about-section").text,
            'provider': banner.find('img').get('src'),
            # 'level': glance.select(''),
            # 'objectives': soup.find('ul', {'class': "Row_nvwp6p"}).findAll('li'),
            'skills': s,
            'instructors': l,

            'link': url,
        }

    return d
