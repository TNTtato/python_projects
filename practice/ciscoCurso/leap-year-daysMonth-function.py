#Define a function that returns True if the year is leap,
#otherwise returns false.
#Define a funtion that returns the number of days in a particular month of
#a particular day, febraury of leap year must be sensitive
#Call the function and give it some test values
#pritn 'OK' if the year matches the conditions stated above and 'Error' if not
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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 12, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	days = testResults[i]
	print(yr, mo, days, "->", end=" ")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
