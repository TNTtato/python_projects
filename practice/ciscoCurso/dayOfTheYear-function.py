#Define a function that returns the day of a year given the values year,
#month and day
def isYearLeap(year):
    if year >= 1582:
        if year%4 != 0:
            validation = False
            return False
        elif year%100 != 0:
            return True
        elif year%400 != 0:
            return False
        else:
            return True
    else:
        return None

def daysInMonth(year, month):
    if isYearLeap(year) != None and month >=1 and month <= 12:
        if isYearLeap(year) and month == 2:
            return 29
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 2:
            return 28
        else:
            return 31
    else: 
        return None

def dayOfYear(year, month, day):
    
    if daysInMonth(year, month) != None and day >= 1 and day <= 31:
        #el viernes (gregoriano) 15 de octubre de 1582
        seedYear = 1582
        seedMonth = 10
        seedDay = 15
        weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dayFound = weekDays[4]
        diffYears = year - seedYear
        for i in range(diffYears):
            currentYear = seedYear + i + 1
            ###Completar proyecto
    else:
        return None


print(dayOfYear(2000, 12, 31))
