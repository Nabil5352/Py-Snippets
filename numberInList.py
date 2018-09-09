# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def createList(number):
    list = []
    current = number
    
    while current > 0:
        remain = current % 10
        list.append(remain)
        current = current/10
    
    return list
    
def numbers_in_lists(string):
    convert = int(string)
    initial = 0
    pushed = []
    final = []
    subArray = []
    current = 0
    
    numberList = createList(convert)
    
    while len(numberList) > 0:
        current = numberList.pop()
        if len(final) > 0:
            if current > initial:
                if initial not in pushed:
                    final.append(initial)
                
                initial = current
                if len(subArray) > 0:
                    final.append(subArray)
                    subArray = []
            else:
                subArray.append(current)
        else:
            initial = current
            final.append(initial)
            pushed.append(initial)
        
        if len(numberList) == 0:
            if initial not in pushed:
                final.append(initial)
                
            if len(subArray) > 0:
                final.append(subArray)
        
    return final

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
