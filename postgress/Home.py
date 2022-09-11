 
import sqlite3
database = sqlite3.connect('SERVER_users.db')
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
def DTA(html):
    
    firstname_1 =  'database = sqlite3.connect'
    father_ =  'database = sqlite3.connect'
    password_ = 'database = sqlite3.connect'
    email_ = 'database = sqlite3.connect'
    Sql.execute("SELECT firstname FROM users WHERE firstname = '{firstname_1}'")
    if Sql.fetchone() is None:
        Sql.execute(f"INSERT INTO users VALUES  (?, ?, ?, ? )",
                    (firstname_1,father_, password_, email_))



database.commit()