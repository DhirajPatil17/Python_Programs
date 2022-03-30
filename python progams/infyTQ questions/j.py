n=int(input())
flag=0
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag is 0:
        print(i)
        
