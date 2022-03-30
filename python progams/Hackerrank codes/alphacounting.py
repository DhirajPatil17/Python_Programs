def encode(message):
    count=0
    l1=[]
    b=sorted(list(set(message)))
    for i in b:
        for j in message:
            if i==j:
                count+=1
        l1.append(str(count))
        count=0
        l1.append(i)
    return "".join(l1)
result=encode("AAAABBBBCCCDDDD")
print(result)


        
