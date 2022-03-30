list1=[1,2,3,4,5,6,['p','y','t','h','o','n']]
print(list1[0:5])
print(list1[5:])
print(list1[6][2])
print(list1[-5])

for fruits in ['apple','banana','pineapple','mango','watermaelon']:
    print("i like:",fruits)

print( 1 in list1)
print(2 not in list1)
list1[0]=0
list1[6][2]='d'
print(list1)


list1.remove(1)
print(list1)
def count(b):
    count1=0
    for i in range(0,len(b)-1):
        if b[i]==b[i+1]:
            count1+=1
        else:
            continue
    return count1
        


a=[1,2,3,3,4,5,6,7]
print(count(a))