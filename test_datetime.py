from datetime import date, datetime , timedelta

#d = date(2021,4,23)
#dt = datetime(2021,4,23,12,30,24)

d = date.today()
#dt = datetime.today()

print(d)
#print(dt)

delta = timedelta(days=5)
date_final = d - delta

print(date_final)

date_str = d.strftime("%d %b %y")

print(date_str)


