import time
import calendar
tickes = time.time()
print(tickes)
print(time.localtime())
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
cal = calendar.month(2019, 1)
print(cal)
print(time.clock())
print(time.timezone)
print(time.tzname)
