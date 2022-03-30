# to insert the int values only in the updated list using isinstance function
x=[1,3.5,None,"6",2,-4]
y=[]
for i in x:
   if isinstance(i,int) and i>0:
       y.append(i)
print(y)


# to print just number not list brackets nor curly braces
s=( i for i in x if isinstance(i,int) and i>0)

print(*s)
# use of zip function
states=["Maharstra","WB","UP","MP"]
capital=["Mumbai","Calcutta","Lucknow","Bhopal"]
print(list(zip(states,capital)))
# use of transpose to unzip the large list elements
transpose=[[1,5,9],[2,6,10],[3,7,11],[4,8,12]]
print(list(zip(*transpose)))

# Use of zip function to add two or more independent list  into a large list
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
print(list(zip(l3,l2,l1)))








