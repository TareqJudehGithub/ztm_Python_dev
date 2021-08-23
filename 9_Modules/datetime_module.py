import datetime


date_now = datetime.datetime.now()
# returns current date
my_date = datetime.date.today()
print(my_date)

# returns a user custom time
my_time = datetime.time(7, 58)
print(my_time)

# returns current year
year = date_now.year
print(year)

# creating custom date objects:
current_date = datetime.datetime(2020, 1, 1)
print(current_date)

# The strftime() Method
#  takes one parameter, format, to specify the format of the returned string.

# More on https://www.w3schools.com/python/python_datetime.asp
# %g returns current year in yy format
time_1 = date_now.strftime('%g')
print(time_1)

# %Y returns current year in yyyy format
time_2 = date_now.strftime('%Y')
print(time_2)

# also try %G for year
time_4 = date_now.strftime('%G')
print(time_4)

# returns AM/PM current time
time_3 = date_now.strftime('%p')
print(time_3)

# returns local version of date

local_time = datetime.datetime.now().strftime('%x')
print(local_time)

# returning custome time or date using more than 1 legal format code:

custom_date = date_now.strftime('%I:%M%p %A %d %Y')
print(custom_date)

# I really like this time format: %c

fav_timef = date_now.strftime('%c')
print(fav_timef)