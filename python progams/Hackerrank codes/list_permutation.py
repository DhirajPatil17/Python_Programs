x=1
y=1
z=2
n=3
l1=[]
l_final=[]
for i in range(0,x+1):
    for j in  range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)!=n:
                l1.append(i)
                l1.append(j)
                l1.append(k)
                l_final.append(l1)
            l1=[]
print(l_final)
                
