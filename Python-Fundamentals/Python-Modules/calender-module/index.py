import calendar

# check methods
# print(dir(calendar))

# create a Month Calnedar
from datetime import datetime

now = datetime.now()
print(now.year, now.month)

# view
from pprint import pprint as pp 
cal  = calendar.monthcalendar(now.year, now.month)
pp(cal)

# first row
cal = calendar.monthcalendar(now.year, now.month+1)
print(cal[0])