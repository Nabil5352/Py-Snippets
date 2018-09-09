# By Ashwath from forums
#
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_square(matrix):
    length = len(matrix)
    final = True
    for i in matrix:
        if len(i) != length:
            final = False
            break
        
    return final, length

def isNotOthersZero(row, principal):
    final = False
    
    for i in range(len(row)):
        if i != principal:
            if row[i] != 0:
                final = True
                break
            
    return final
    
def is_identity_matrix(matrix):
    final = True
    isSquare, size = is_square(matrix)
    principal_diagonal = 0
    
    if isSquare:
        for i in matrix:
            if i[principal_diagonal] != 1 or isNotOthersZero(i, principal_diagonal):
                final = False
                break
            else:
                principal_diagonal += 1
    else:
        final = False
        
    return final
    
# Test Cases:
matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,1],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           

           