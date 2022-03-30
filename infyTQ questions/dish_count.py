


no_of_testcase=int(input())
res=[]
for tc in range(no_of_testcase):
    no_of_array_elements=int(input())
    l1=list(map(int,input().split()))[:no_of_testcase]
    i=0
    max=0
    Item_type=l1[0]
    while i<no_of_array_elements:
        count=1
        j=i+1
        while(j<no_of_array_elements):
            if l1[i]==l1[j] and j!=i+1:
                count+=1
                if j<no_of_array_elements-1 and l1[j]==l1[j+1]:
                    j+=1
            j+=1
        if max<count:
            max=count
            Item_type=l1[i]
        i+=1
        res.append(Item_type)
for tc in range(no_of_testcase):
    print(res[tc])


    