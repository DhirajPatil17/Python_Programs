# uses of lamda function,map function, filter function
even=[i for i in range(1,11) if i%2==0]
print(even)

def even_dig(x):#using map function
    
    return x%2==0
number=list(range(1,11))
print(list(map(even_dig,number)))

def even_dig(x):#using filter function it shows only true values which means even values
    
    return x%2==0
number=list(range(1,11))
print(list(filter(lambda x:x%2==0,number)))

number=list(range(1,11))#  using lambda function
print(list(filter(lambda x:x%2==0,number)))

houses=["Slytherin","Gryffindor","Ravenclaw","Hufflepuff"]
lenght=[i for i in houses if len(i)>=10]
print(lenght)

final=(list(filter(lambda x:len(x)>=10, houses)))# using filter function
print(final)
 
l1=[1,2,3]
l2=l1[:]
print(id(l1)) 
print(id(l2))
print(l1 is l2)

inp =[1,2,3,4,5]
l2=[]
sum2=0
for i in inp:
    sum2=sum2+i
    l2.append(sum2)
    print(l2)
print([sum(inp[:i+1]) for i in range(0,len(inp))])
  
