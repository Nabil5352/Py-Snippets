# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#


def count(num, number):
    counter = 0
    
    while True:
        prev = number
        current = number - num
        number = current
        
        if current < 0:
            remain = current
            break
        else:
            counter = counter + 1
    
    return counter, prev

def stamps(number):
    remaining = number
    
    if number<1:
        return (0,0,0)
        
    counter5, remaining5 = count(5, remaining)
    counter2, remaining2 = count(2, remaining5)
    counter1, remaining1 = count(1, remaining2)
    
    return counter5, counter2, counter1

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps