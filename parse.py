import dateutil.parser
import requests
from bs4 import BeautifulSoup
page = 0

# HOST = 'https://www.kijiji.ca/h-city-of-toronto/1700273'
HOST = 'https://www.kijiji.ca'
HOSTS = 'https://media.kijiji.ca/api/v1/ca-prod-dealer-ads'
HEADERS = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
while True:
    URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-'+ str(page) + '/c37l1700273'
    page += 1
    if page == 93:
        break
    def get_html(url, params=''):
       r = requests.get(url, headers=HEADERS, params=params)
       
       return r
 
    def get_content(html):

        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='search-item')
        shop = []
        for item in items:
            loc = item.find('div', class_='location')
            pucture = item.find('div', class_='image')
            bed = item.find('div', class_='rental-info')
            
 
         
            shop.append(
            { 
            'image':   item.find('div', class_='image').find('img').get('src'),

            'title': item.find('div', class_='title').get_text(strip=True),
            'link': HOST + item.find('div', class_='title').find('a').get('href'),
            'price': item.find('div', class_='price').get_text(strip=True),
            'location': item.find('div', class_='location').find('span').get_text(strip=True),
            'description': item.find('div', class_='description').get_text(strip=True),
            'bedroom': bed.find('span', class_='bedrooms'),
            'date':  loc.find('span', class_='date-posted').get_text(strip=True), })
        return shop
    
    htmls = get_html(URL)
    print(get_content(htmls.text))




 
