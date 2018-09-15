# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(value):
    hour = 0
    minute = 0
    second = 0
    hourTxt = ' hours, '
    minuteTxt = ' minutes, '
    secondTxt = ' seconds'
    
    if value >= 60:
        hour = int(value/(60*60))
        value -= hour*60*60
        minute = int(value/60)
        value -= minute*60
        second = round(value, 1)
    else:
        second = value*1.0
        
    #check if a float value is a whole number
    if second.is_integer():
        second = int(second)
    
    if hour == 1:
        hourTxt = ' hour, '
        
    if minute == 1:
        minuteTxt = ' minute, '
        
    if second == 1:
        secondTxt = ' second'
    
    return `hour` + hourTxt + `minute` + minuteTxt + `second` + secondTxt


print convert_seconds(1)
#>>> 0 hour, 0 minute, 1 second

print convert_seconds(3660)

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds