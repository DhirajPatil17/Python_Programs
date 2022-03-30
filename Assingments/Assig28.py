#product of unique elements
l1=[10,20,30,40,20,50,60,40]
l2=[]
l2=list(set(l1))
count=0
pro=1
for i in l2:
    for j in l1:
        if i==j:
            count+=1
    if count>1:
        l2.remove(i)
        count=0
    count=0
print(l2)
for i in l2:
    pro*=i
print(pro)