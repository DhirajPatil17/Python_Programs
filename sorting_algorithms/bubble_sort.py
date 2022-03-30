list1=[10,15,4,2,23,0]
print("Unsorted list:",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print()
print("sorted lsit",list1)

#step 1: its very simple 
#step 2:just use two for loop outer loop will traverse till len(list1)-1
#step 3:inner loop traverse till len(list1)-1-j (beacuse on every  iteration list element is going to be left behind because its going to be the largest elements among the unsorted list)
#step 4:we have to check weather the first element is greater element 
#step 5: if yes then exchange the position of them 
#step 6: if not then increment the element