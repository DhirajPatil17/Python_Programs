str1="hallo"
sl="llo"
count=0
for i in range(len(sl)):
    for j in range(len(str1)):
        if sl[i]==str1[j]:
            count+=1
            j=j+2
print(count)
        



