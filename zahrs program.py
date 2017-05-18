import datetime

name = str(input('Enter your name:'))
date = int(input('Enter your date of birth:'))
month =int(input('Enter your month of birth:'))
age = int(input('what is your age?'))

days_per_year = 365.24
currentdate = datetime.datetime.now()
age2 = datetime.timedelta(days = (age*days_per_year))
year_of_birth = currentdate - age2
year_of_birth2 = int(year_of_birth.strftime('%Y'))
day_of_the_week = datetime.date(year_of_birth2,month,date)
print(day_of_the_week.strftime('%A'))                    
                  
