def insertion_sort(list1):
    for index in range(1,len(list1)):
        current_element=list1[index]
        pos=index
        while current_element<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
list1=[10,4,25,1,5]
insertion_sort(list1)
print(list1)
# step 1: take list in loop and start from 1 position to len(list) 
# step 2: then take current_element=list1[index]
# step 3: then store index in pos variable
# step 4: Iterate until current<list[pos] and pos>0 
# step 5: In iteration put list1[pos]=list1[pos-1] and pos=pos-1
# step 6: once the loop terminates list1[pos]=current_element





