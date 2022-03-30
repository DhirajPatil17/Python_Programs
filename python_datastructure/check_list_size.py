import sys
# def list_details(list):
#     print("Capacity:",(sys.getsizeof(list)))#To Check capacity
#     print("length is:",len(list))# To check length
#     print("Space_left:",((sys.getsizeof(list)-36)-len(list*4))//4)# check space left
list1=[1,2,3,4,5,6,7,8,9,1,2,3,3,4,5,2,6,3,7,8,8,9,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1]
print((sys.getsizeof(list1)-64)//4)
# print("Empty list created")
# print("List details")
# list_details(list1)