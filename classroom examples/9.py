#Date Time
from datetime import datetime
d=datetime.now()
print( d)
print( d.year)
print( d.month)
print( d.day)
print( d.hour)
print( d.minute)
print( d.second)


print(d.strftime('%A %d. %B %Y'))
print(d.strftime('%d/%m/%y'))


a=datetime.today()
b=datetime(1947,8,15)

print((a-b).days)
