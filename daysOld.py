# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no time travel). 
#

def isLeapYear(year):
    # Source:https://en.wikipedia.org/wiki/Leap_year#Algorithm
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        final = True
    else: 
        final = False
        
    return final
    

def daysOfMonth(month, year):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #list of days according to their months
    
    isLYear = isLeapYear(year)
    
    index = month-1
    final = daysOfMonths[index]
    
    if index == 1: #February
        if isLYear: #if leap year return 29days
            final=29
            
    return final
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    # initialize
    dayofMonth = 0
    dayOfYear = 365
    
    # CHECK YEAR
    diffYear = year2-year1
    if diffYear == 0:   #if same year total day = 0
        dayOfYear = 0
    elif diffYear > 0:  #if not same year loop between years and count days
        totalDay = 0
        counter = 0
        counterYear = year1;
        while counter < diffYear+1:
            isLYear = isLeapYear(counterYear) #check if leap year
            if isLYear:
                totalDay = totalDay+1 #add 1 day if leap year
            counter = counter+1
            counterYear = counterYear+1 #increment year

        dayOfYear = dayOfYear*diffYear+totalDay #total year + extra days for leap year

    # CHECK MONTH
    diffMonth = month2-month1
    if diffYear == 0 and diffMonth == 0: #if same year and same month
        dayofMonth = 0
    elif diffMonth == 1: #if last month is the next month
        daysofmonth1 = daysOfMonth(month1,year1) #total days of the first month
        monthDay1 = daysofmonth1-day1 #remaining days of the first month
        monthDay2 = day2 #only days of the last month
        
        dayofMonth = monthDay1+monthDay2 #total days
    elif diffMonth > 1: #if last month is more than next month
        currentMonth = month1 #save current month
        totalDayofMonth=0
        while currentMonth != month2-1: #in loop exclude first and last month(calculated later) and loop inside them
            dayofMonth = daysOfMonth(currentMonth+1,year1) #find days of current month
            totalDayofMonth = totalDayofMonth + dayofMonth #add them
            currentMonth=currentMonth+1 #increment current month
            dayofMonth=0 #reinitialize total days of a month
        
        # calculate first and last month
        daysofmonth1 = daysOfMonth(month1,year1) #total days of the first month
        monthDay1 = daysofmonth1-day1 #remaining days of the first month
        monthDay2 = day2 #only days of the last month
        
        dayofMonth = totalDayofMonth+monthDay1+monthDay2 #total days
    
    final = dayOfYear+dayofMonth #final calculation = Total days of the year + Total days of the month
    return final

# Test cases
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
