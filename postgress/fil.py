 
# import sqlite3
# database = sqlite3.connect('SERVER.db')
# Sql = database.cursor()
# Sql.execute(
#     """
#     CREATE TABLE users(
#     image TEXT,
#     title TEXT,
#     link TEXT,
#     location TEXT
#     )
#     """
# )
# database.commit()

# # firstname_1 =    '09/09/2022', '08/09/2022', '13/08/2022', '29/08/2022', '30/08/2022', '12/12/12', '12/12/12', '12/12/12', '12/12/12'

# firstname_1 = 'Hello'
# # father_ =   '09/09/2022', '08/09/2022', '13/08/2022', '29/08/2022', '30/08/2022', '12/12/12', '12/12/12', '12/12/12', '12/12/12'
# # password_ =  '09/09/2022', '08/09/2022', '13/08/2022', '29/08/2022', '30/08/2022', '12/12/12', '12/12/12', '12/12/12', '12/12/12'
# # email_ =  '09/09/2022', '08/09/2022', '13/08/2022', '29/08/2022', '30/08/2022', '12/12/12', '12/12/12', '12/12/12', '12/12/12'
# # for i in str(firstname_1):
# # Sql.execute("SELECT firstname FROM users WHERE firstname = '{firstname_1}'")
# if Sql.fetchone() is None:
#     Sql.execute(f"INSERT INTO users VALUES  (?, ?, ?, ? )",
#                     (firstname_1,firstname_1, firstname_1, firstname_1))



# database.commit()
 


# m = 0
# mil = ['1','2','3','4','5','25','3','45']
# mil = ['minute ago', 'hours ago']
# min = []
# lin = []
# date = [['09/09/2022'],['08/09/2022'],['13/08/2022'],['29/08/2022'],['30/08/2022'],['< 35 minute ago'],['< 1 minute ago'],['< 6 minutes ago'],['< 7 minutes ago']]

# m += len(date)
 
# for i in date:
#     for l in i:
#         # print(l)
#         if l[m-1] in 'minute ago' and  'hours ago':
#             min.append(l)
#         else:
#             lin.append(l)
            
             
            
 
# for i in min:
#     mins = i.replace(i, '12/12/12')
#     lin.append(mins)
# print(lin)
min = []
lin = []
date = '09/09/2022','08/09/2022','13/08/2022','29/08/2022','30/08/2022','< 35 minute ago','< 1 minute ago','< 6 minutes ago','< 7 minutes ago'


for i in date:
    if i[0+1] in 'minute ago' and  'hours ago':
          min.append(i)
    else:
          lin.append(i)

for i in min:
    mins = i.replace(i, '12/12/12')
    lin.append(mins)

for dates in lin:
      pass
 
 
 
            
     