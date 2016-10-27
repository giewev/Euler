from datetime import date
from datetime import timedelta

current = date(1901, 1, 1)
last = date(2000, 12, 31)
sunday_count = 0
while current <= last:
	if current.weekday() == 6 and current.day == 1:
		sunday_count += 1
	if current.month == 12:
		current = current.replace(month = 1, year = current.year + 1)
	else:
		current = current.replace(month = current.month + 1)

print(sunday_count)