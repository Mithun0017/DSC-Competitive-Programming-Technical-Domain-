# Competive Programming
# Problem 3
'''
Name : Mithun. T
Programme : B.Tech(CSE)
Section : 'D'
Year : 1st year
Register No. : RA2411003020254
'''

from datetime import datetime, timedelta # !!!Kindly install the datetime module in pip(if not available)

def generate_date(no_of_days, year):
    day = datetime(year, 1, 1)
    date = day + timedelta(days=no_of_days - 1)
    date_string = date.strftime("%d %B, %Y")
    return date_string

no_of_days = int(input("Enter the no. of days : "))
year = int(input("Enter the year : "))
print(generate_date(no_of_days, year))
