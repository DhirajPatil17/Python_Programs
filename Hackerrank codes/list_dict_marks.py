# aam zindagi 
n=int(input())
d1={}
for i in range(n):
    keys=input()
    no_of_subjects=int(input("No of subjects:"))
    marks=[]
    for i in range(3):
        marks.append(int(input()))
    d1[keys]=marks
sum=0
Query=input()
for keys,values in d1.items():
    if Query  in d1.keys():
        for i in d1[Query]:
            sum+=i
        c=sum/3
        print(round(c,2))    
        break
       
    else:
        print("Not available")
        break
from decimal import Decimal

# mentos zindagi
d1={}
n=int(input())
for i in range(n):
    name,*line=input().split()
    scores=list(map(float,line))
    d1[name]=scores

Query=input()
for keys,values in d1.items():
    if Query  in d1.keys():
        c=sum(d1[Query]) 
        avg=Decimal(c/3)
        print(round(avg,2) )
        break
       
    else:
        print("Not available")
        break


