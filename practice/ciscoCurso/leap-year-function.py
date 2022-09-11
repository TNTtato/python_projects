#Define a function that returns True if the year is leap,
#otherwise returns false. Call the function and give it some test values
#pritn 'OK' if the year matches the condition stated above and 'Error' if not

def isYearLeap(year):
    if year >= 1582:
        if year%4 != 0:
            validation = [False, "Comun year"]
            return validation
        elif year%100 != 0:
            validation = [True, "Leap Year"]
            return validation
        elif year%400 != 0:
            validation = [False, "Comun year"]
            return validation
        else:
            validation = [True, "Leap Year"]
            return validation
    else:
        validation = [None, "Not in gregoryan calendary"]
        return validation

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end=" ")
	result = isYearLeap(yr)
	if result[0] == testResults[i]:
		print("OK", result[1])
	else:
		print("Error", result[1])
