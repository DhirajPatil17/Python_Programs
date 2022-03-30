
# Use of the counter function to count the repetation of alpabets
from collections import Counter
c=Counter("aldhidhewiodewoidx")
print(c)


# Sum of the digits of the numbers
def check(number1):
    sum=0
    d=0
    while(number1!=0):
        d=number1%10
        number1=number1//10
        sum=sum+d
    return sum

num=check(123)
print(num)
