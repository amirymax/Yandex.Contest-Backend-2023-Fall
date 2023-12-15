from datetime import datetime
year1, month1, day1, hour1, min1, sec1 = map(int,input().split())
year2, month2, day2, hour2, min2, sec2 = map(int,input().split())

days = (year2 - year1) * 365

date1 = datetime(1, month1, day1, hour1, min1, sec1)
date2 = datetime(1, month2, day2, hour2, min2, sec2)

difference = date2 - date1
days += difference.days
print(days, difference.seconds)