# l1=[]
# n=5
# l_final=[]
# count=0
# for i in range(n):
#     l1.append(input("Enter the name"))
#     l1.append(int(input("Marks")))
#     l_final.append(l1)
#     l1=[]

# for i in l_final:
#     for j in l_final:
        
#         if i[1]<=j[1]:
#             count+=1
#         if count==n:
#             print(i[0])
        
#     count=0
# for the lowest score

l1=[]
l2=[]

l_final=[]
count=0
l_final=[['Hina', 20], ['Shina', 20.1], ['Mina', 20.01], ['Tina',20.001]]
for i in l_final:
    l2.append(i[1])
c=sorted(list(set(l2)))
print(c)


d=sorted(l_final)
for i in d:
    if i[1]==c[1]:
        print(i[0])

    
    
  
        




    
#second lowest score



    
    

        


