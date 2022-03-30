s=int(input())
l1=list(str(s))
l2=[]
count=0
d=list(set(str(s)))
for i in d:
    for j in l1:
        if i==j:
            count+=1
    if count>1:
        l2.append(count)
        count=0
    else:
        count=0
print(len(l2))

    


        
        

        

