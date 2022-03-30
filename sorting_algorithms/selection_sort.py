list1=[2,34,3,12,2,5,5,4]
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)# this code is for duplicate values in list 
    list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)
