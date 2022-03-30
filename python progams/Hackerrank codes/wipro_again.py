n=int(input())
l1=list(map(int,input().strip().split()))

l2=[]
for i in l1:
    if i>0:
        l2.append(i)
l3=(list(set(l2)))
l4=sorted(l3)
sum=l4[len(l3)-1]+l4[len(l3)-2]
print(sum)

    


    
    



  