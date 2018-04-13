import sys
from datetime import date
from datetime import timedelta

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = date(year, month, day)

today = date.today()
print("Dzisiejsza data : " + str(today))
print("Podana data: " + str(date1))

date2 = today - date1

print("Różnica dat: " + str(date2))