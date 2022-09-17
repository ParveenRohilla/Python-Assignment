# Write a Python program which takes two digits m (row) and n (column) as input
# and generates a two-dimensional array. The element value in the i-th row
# and j-th column of the array should be i*j.

# Note :

# i = 0,1.., m-1

# j = 0,1, n-1.


m=int(input("Row:"))
n=int(input("Column:"))
two_d_array =[[0 for col in range(n)] for row in range(m)]
for row in range(m):
    for col in range(n):
        two_d_array[row][col]=row*col
print(two_d_array)
