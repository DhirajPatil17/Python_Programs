rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of columns"))
matrix1=[]
for i in range(rows):
    a=[]
    for j in range(column):
        a.append(int(input()))
    matrix1.append(a)
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        print(matrix1[i][j],end=' ')
    print()