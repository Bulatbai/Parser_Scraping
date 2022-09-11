  
import requests
import csv
from bs4 import BeautifulSoup
import sqlite3

CSV = 'csv.shop'
database = sqlite3.connect('Parser.db')
Sql = database.cursor()

Sql.execute(
    """
    CREATE TABLE users(
    image TEXT,
    title TEXT,
    link TEXT,
    location TEXT,
    date TEXT,
    bed TEXT,
    description TEXT,
    price TEXT

    )
    """
)
database.commit()


 




HOST = 'https://www.kijiji.ca'
HOSTS = 'https://media.kijiji.ca/api/v1/ca-prod-dealer-ads'
HEADERS = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}   

 
    

 
 


page = int(input('Укажите количечтва страниц до 93>>'))
while True:
  
    URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-'+ str(page) + '/c37l1700273'
    page -= 1
    if page == -1:
        break
    def get_html(url, params=''):
        r = requests.get(url, headers=HEADERS, params=params)
       
        return r
 
    def get_content(html):
            
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='search-item')
        shop = []
        price = []
       
        for item in items:

            loc = item.find('div', class_='location')
            beds = item.find('div', class_='rental-info')
            image = ''
            title = ''
            link = ''
            location = ''
            date = ''
            bed = ''
            description = ''
            price = ''
            image += (item.find('div', class_='image').find('img').get('src'))
            title += (item.find('div', class_='title').get_text(strip=True))
            link += (HOST + item.find('div', class_='title').find('a').get('href'))
            location += (item.find('div', class_='location').find('span').get_text(strip=True))
            date += (loc.find('span', class_='date-posted').get_text(strip=True))
            bed  += (beds.find('span', class_='bedrooms').get_text(strip=True))
            description += (item.find('div', class_='description').get_text(strip=True))
            price += (item.find('div', class_='price').get_text(strip=True))
            
            print(date)
            min = []
            lin = []
            datek = '09/09/2022','08/09/2022','13/08/2022','29/08/2022','30/08/2022','< 35 minute ago','< 1 minute ago','< 6 minutes ago','< 7 minutes ago'


            # for i in datek:
            if date[0+1] in 'minute ago' and  'hours ago':
                min.append(date)
            else:
                lin.append(date)

            for i in min:
                mins = i.replace(i, '12/09/2022')
                lin.append(mins)

            for dates in lin:
                
               location = str(location)
               if Sql.fetchone() is None:
                    Sql.execute(f"INSERT INTO users VALUES  (?, ?, ?, ?, ?, ?, ?, ? )",
                    ( image, title,  link, location,dates, bed, description, price ))
            database.commit()
          
            shop.append(
            { 
            'image':   item.find('div', class_='image').find('img').get('src'),
            'title': item.find('div', class_='title').get_text(strip=True),
            'link': HOST + item.find('div', class_='title').find('a').get('href'),
            'price': item.find('div', class_='price').get_text(strip=True),
            'location': item.find('div', class_='location').find('span').get_text(strip=True),
            'description': item.find('div', class_='description').get_text(strip=True),
            'bedroom': beds.find('span', class_='bedrooms').get_text(strip=True),
            'date':  loc.find('span', class_='date-posted').get_text(strip=True), 
            })
         
        return shop  
          
           
        
            
            
            
    def save_dock(items, path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['pucture', 'title', 'link', 'price', 'location', 'description','bedroom', 'date'])
            for item in items:
                writer.writerow([item['image'],
                item['title'],item['link'],item['price'],item['location'],
                item['description'],item['bedroom'],
                item['date']]
                )

         
           
    
    def parser():
        PAGENATION = input("Укажите количечтва страниц до 93 для Parsinga>")
        PAGENATION = int(PAGENATION.strip())
            
        htmls = get_html(URL)
        
        if htmls.status_code == 200:
            cards = []
            for page in range(1, PAGENATION+1):
                print(f'loading>{page}')
                html = get_html(URL, params={'page': page})  
                cards.extend(get_content(html.text))
                save_dock(cards, CSV)

            pass
        else:
            print('error')
    parser()


