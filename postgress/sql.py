 

import sqlite3
database = sqlite3.connect('Parser.db')
Sql = database.cursor()
 
Sql.execute(
    """
    CREATE TABLE users(
    image TEXT,
    title TEXT,
    link TEXT,
    location TXT,
    date INT,
    bed INT,
    description TEXT,
    price INT

    )
    """
)
database.commit()
# image =  [item.find('div', class_='image').find('img').get('src')]
# title =  item.find('div', class_='title').get_text(strip=True)
# link =  HOST + item.find('div', class_='title').find('a').get('href')
# location =  item.find('div', class_='location').find('span').get_text(strip=True)
# date =  loc.find('span', class_='date-posted').get_text(strip=True)
# bed =  bed.find('span', class_='bedrooms').get_text(strip=True)
# description =  item.find('div', class_='description').get_text(strip=True)
# price =  item.find('div', class_='price').get_text(strip=True)
# Sql.execute("SELECT firstname FROM users WHERE firstname = '{id}'")
# if Sql.fetchone() is None:
#     Sql.execute(f"INSERT INTO users VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#             (id, image, title, link, location, date, bed, description, price ))


# class Parsing:
    
page = int(input('Укажите количечтва страниц>>'))
 
    # def __init__(self, image, title, link, location, date, description, bed, price ):
    #     self.image =  image
    #     self.title = title
    #     self.link = link
    #     self.location = location
    #     self.date = date
    #     self.description = description
    #     self.bed = bed
    #     self.price = price