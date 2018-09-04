#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 

def findValues(value):
    values = []
    final = []
    curr = value
    
    while curr != 0:
        remain = curr%10
        curr = curr/10
        values.append(remain)
    
    for i in reversed(values):
        final.append(i)
        
    return final

def formatItm(abacus, item):
    space = "   "
    final = ""
    data = list(abacus)
    length = len(data)
    
    for index,val in enumerate(range(length)):
        if index == length-item-1:
            deta = data[index]+space
        else:
            deta = data[index]
   
        final = final+deta
        
    return final

def print_abacus(value):
    abacus = "00000*****"
    space = "   "
    border = "|"
    allValues = []
    
    if value > 0:
        allValues = findValues(value)
        
    length = len(allValues)

    if length > 0:
        start = 10 - length
        iterate = 0
        for index,val in enumerate(range(10)):
            if index == start:
                item = allValues[iterate]
                formatItem = formatItm(abacus, item)
                print border+formatItem+border
                start = start+1
                iterate = iterate+1
            else:
                print border+abacus+space+border
    else:
        for _ in range(10):
            print border+abacus+space+border
            

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|