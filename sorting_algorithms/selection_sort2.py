input_list=[33,15,27,8,35,42,19,48]
size=len(input_list)
for num in range(0,size-1):
    min_value_index=num
    for val in range(num+1,size):
        if input_list[val]<input_list[min_value_index]:
            min_value_index=val
    if min_value_index!=num:
        temp=input_list[num]
        input_list[num]=input_list[min_value_index]
        input_list[min_value_index]=temp
print(input_list)