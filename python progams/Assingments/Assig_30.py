#1: Permutations
from itertools import permutations as pm
l1=pm([1,2,3])
for i in list(l1):
    print(i,end=" ")

from dataclasses import replace

# Check Alpha
s="Hello this is dhiraj pursuing engg in SVKM IOT DHULE" 
g=s.replace(" ","")
print(g.isalpha())

#Half sort ascending and half sort decending
l1=[5,2,4,7,9,3,1,6,8]
l2=[]
l3=[]
l5=[]
mid=len(l1)//2
l2=sorted(l1)
for i in range(0,mid):
    l5.append(l2[i])
for i in range(len(l2)-1,mid-1,-1):
    l3.append(l2[i])
print(l5+l3)










    