n=int(input("enter the number of list items"))
l1=[]
for i in range(n):
    i=input("enter the users email:")
    l1.append(i)
print(l1)
l2=[]
for j in range(len(l1)):
    if l1[j] not in l2:
        l2.append(l1[j])
    else:
        pass
print(l2)

    
    
