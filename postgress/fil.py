 
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
 
 
 
# from ast import While

# min = []
# lin = []
# min1 = []
# m  = [] 
# lin1 = []

 

# minute = []
# dates = '09/09/2022','08/09/2022','13/08/2022','29/08/2022','30/08/2022','< 24 hours ago',\
# '< 1 minutes ago','< 6 minutes ago','< 7 minutes ago','< 20 hours ago',\
# '< 13 hours ago', '< 12 hours ago','< 2 hours ago', '< 10 minutes ago'
# all = []
# ones = []
# strings = []
# def set_up_date(date):
#    for i in date:
#       if i[0+1] in f'<  hours ago':
#          min.append(i)
#       else:
#          lin.append(i)
#    for i in  min:
#       mins = i.replace(f'hours ago',  '')
#       min1.append(mins)
#    for i in min1:
#       mins3 = i.replace(f'<', '')
#       minute.append(mins3)
#    for i in minute:
#       strings.append(i[::-1])
#    for i in strings:
#       if i[0+1] in 'oga setunim':
#          all.append(i)
#       else:
#          ones.append(i)
#    for i in ones:
#       m.append(int(i[::-1]))
#    d1 = datetime.date.today()
#    d = 0
#    for i in m:
       
     
#   print(i)
        
#    return date
# set_up_date(dates) 
# 


   # for i in bigfree:
   #    if i[0+1] in 'oga setunim':
   #       MInutes.append(int(i[::-1].replace('minutes ago', '')))
   
   #    else:
   #       Hours.append(int(i[::-1]))
   
 
 

    








import datetime

dates = '09/09/2022','08/09/2022','13/08/2022','29/08/2022','30/08/2022','< 24 hours ago',\
'< 1 minutes ago','< 6 minutes ago','< 7 minutes ago','< 20 hours ago',\
'< 13 hours ago', '< 12 hours ago','< 2 hours ago', '< 10 minutes ago'

hoursago = []
normformat_date = []
better = []
bigfree = []
def SetUp(datess):
   for i in datess:
      if i[0+1] in '< hours ago':
         hoursago.append(i)
      else:
         normformat_date.append(i)
   
   for i in hoursago:
      better.append(i.replace('hours ago', '',))
  
  
   for i in better:
       bigfree.append(i[::-1].replace('<', ''))
   MInutess = []

   for i in bigfree:
      MInutess.append(int(i[::-1].replace(' minutes ago', '00')))
   data3 = datetime.datetime.now()
   print(data3)
   data = datetime.date.fromordinal(738412)
   print(data.strftime("%d/%m/%Y"))
   OST = [int(i/100) for i in MInutess   if i > 24 ]
   print(OST)
   OSTI = []
   
   for i in MInutess:
      OSTI = int(i/100) if i > 24 else i * 1
      data = datetime.date.fromordinal(738412)
      OSTT = datetime.date.fromordinal(int(738412-i) if i > 24 else 738412-i)
      normformat_date.append(OSTT.strftime("%d/%m/%Y"))
   
   return datess
SetUp(dates)  
        


  


 
    



 
 
 

 

 
 
 





 
 

      


