page = 1
while True:
    if page == 93:
        break
    page += 1
    URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-'+ str(page) + '/c37l1700273'
    print(URL)