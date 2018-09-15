# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
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
        second = value*1.0
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
    
def convert(unit):
    final = 0
    
    if unit == 'kb':
        final = 2 ** 10
    elif unit == 'kB':
        final = 2 ** 10 * 8
    elif unit == 'Mb':
        final = 2 ** 20
    elif unit == 'MB':
        final = 2 ** 20 * 8
    elif unit == 'Gb':
        final = 2 ** 30
    elif unit == 'GB':
        final = 2 ** 30 * 8
    elif unit == 'Tb':
        final = 2 ** 40
    elif unit == 'TB':
        final = 2 ** 40 * 8
        
    return final

def download_time(file_size, size_unit, bandwidth, bandwidth_unit):
    total = (file_size * convert(size_unit) * 1.0)/(bandwidth * convert(bandwidth_unit))
    return convert_seconds(total)

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 37 minutes, 32.8 seconds

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


