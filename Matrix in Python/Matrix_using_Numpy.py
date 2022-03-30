import numpy as np
matrix1=np.array([[1,2,3],[2,3,4],[4,5,6]])
matrix2=np.array([[4,5,2],[12,6,4],[8,6,5]])
#Matrix addition
matrix3=matrix1+matrix2
print(matrix3)
#matrix sustraction
matrix3=matrix1-matrix2
print(matrix3)
#matrix multiplication
matrix3=matrix1*matrix2
print(matrix3)
#matrix slicing
matrix5=np.array([1,2,3,3,4])
print(matrix5[2:5])
matrix4=np.array([[1,2,3,3,4],[2,3,4,1,2],[4,5,6,3,4]])
print(matrix4[1:3,1:5])# first slice for row numbers[1:3] and second slice is for choosing starting and ending point for rows elements
print(matrix4[:1,])
