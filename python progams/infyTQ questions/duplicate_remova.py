

str="222233435657uwqtqasda!"
count=0
l2=[]
for i in str:
    for j in str:
        if i==j:
            count+=1
        if count>0:
            if i not in l2:
                l2.append(i)
            
                break
    count=0
print("".join(l2))

            
    