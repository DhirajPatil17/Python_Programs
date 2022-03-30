#matrix_transpose
matrix1=[[12,23,34],[67,89,12]]
matrix2=[[0,0],[0,0],[0,0]]
# using simple method 
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix2[j][i]=matrix1[i][j]
for i in range(len(matrix2)):
    print(matrix2[i])
# using list comprehension method
matrix2=[[matrix1[j][i] for j in range(len(matrix1))]for i in range(len(matrix1[0]))]
print(matrix2)