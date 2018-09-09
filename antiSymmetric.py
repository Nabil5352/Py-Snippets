# By Dimitris_GR from forums
# 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(array):
    final = True
    init_list = []
    second_list = []
    
    #check if array is not empty
    if len(array) > 0:
        counter = 0
        for i in array:
            #assign a single row
            init_list = i 
            # assign corrseponding column
            for j in array:
                second_list.append(j[counter])
            
            #if length doesn't match then they are not symmetrical
            if len(init_list) == len(second_list):
                #contiously check and exit if doesn't match
                if final == False:
                    break

                #match both list
                for k in range(len(init_list)):
                    #convert to negative of current number
                    test_val = second_list[k] - (second_list[k]+second_list[k])
                    if init_list[k] != test_val:
                        final = False
    
                second_list = []
                counter += 1
            else:
                final = False
            
    return final


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
