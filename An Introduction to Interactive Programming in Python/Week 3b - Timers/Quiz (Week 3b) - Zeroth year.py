import time

time_ellapsed = time.time()
seconds = time_ellapsed % 60
minutes = (time_ellapsed // 60) % 60
print time_ellapsed

hours = (time_ellapsed // 3600) % 24
print hours

days = (time_ellapsed // (3600 * 24)) % 365 
print days

years = (time_ellapsed // (3600 * 24 * 365)) 
print years

print 
print years,days,hours,minutes,seconds

current_year = 2014

zeroth_year = current_year - years

print zeroth_year