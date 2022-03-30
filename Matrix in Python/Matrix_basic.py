# Matrix Addition
matrix1=[[45,21,90],[24,44,100],[23,21,54]]
matrix2=[[123,21,90],[67,44,100],[7,21,54]]
matrix3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print("Your Addition:",matrix3)

# Matrix Substraction

matrix3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j]=matrix1[i][j]-matrix2[i][j]
print("Your Substration:",matrix3)
# Matrix Multiplication

matrix3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j]=matrix1[i][j]*matrix2[i][j]
print("Your Multiplication is:",matrix3)
# Matrix Division

matrix3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        matrix3[i][j]=matrix1[i][j]//matrix2[i][j]
print("Your division is:",matrix3)
