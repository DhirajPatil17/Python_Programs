list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']
list3=[]
str2=""
for i in list1:
    for j in list2:
        c=list2.pop()
        if c is None:
            str2=i
        elif i is None:
            str2=c
        else:
            str2=i+c
        list3.append(str2)
        break
print(" ".join(list3))
        


