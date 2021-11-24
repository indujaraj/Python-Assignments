import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(1)
tomorrow=today+datetime.timedelta(1)
print("today is",today)
print("yesterday is",yesterday)
print("tomorrow is",tomorrow)
