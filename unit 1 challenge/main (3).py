
def isleapYear(year):
  if (year % 4 == 0 and year % 100 !=0) or year % 400 ==0:
    return True
  else:
    return False

year = 2012

if isleapYear(year):
  print('{} is a loop year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))