def pivot_place(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivot:
            left=left+1
        while left<=right and list1[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right
def quick_sort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
list1=[56,26,93,17,31,44]
n=len(list1)
quick_sort(list1,0,n-1)
print(list1)

# step 1 is to get the rightplace for the pivot element 
# then divide the list into two from the new pivot+1 to last and first to pivot-1
# again repeat the same process

