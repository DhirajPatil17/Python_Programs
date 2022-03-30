l1=[]
n=int(input("how many elements you want to enter"))
for i in range(0,n):
    l1.append(int(input("Enter the list items")))
ch=0
while(ch<4):
    ch=int(input("which operation do you want ot perform \n 1.Add operation \n 2: Insert operation \n 3: Pop operation" ))
    if ch == 1:
        n=int(input("Enter the number you want to add"))
        l1.append(n)
        print(l1)
    elif ch == 2:
        n=int(input("Enter the number you want to enter"))
        p=int(input("Enter the position you want to enter"))
        if p <=len(l1):
            l1.insert(p,n)
            print(l1)
        else:
            print("Index out of bound")
    elif ch == 3:
        p=int(input("Enter the index number you want ot delete"))
        if p <=len(l1):
            l1.pop(p)
            print(l1)
        else:
            print("Index out of bound")
    else:
        print("Exit")
        exit

        


