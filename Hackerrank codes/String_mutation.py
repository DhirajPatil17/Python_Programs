# string manipulation
# s=input()
# p=int(input())
# c=input()
# l1=list(s)
# l1[:5]+c+l1[6:]
# print("".join(l1))

# Sub string Counting
from gettext import find


string="TestCaseTestCase"
sub="CaseT"
l1=[]
count=0
# update="".join(set(sub.casefold()))
d=string.find(sub)
for i in sub:
    if len(sub)%2!=0:
        for j in range(d,len(string)):
            if i ==string[j]:
                count+=1
        l1.append(count)
        count=0
        m=min(l1)
        
    else:
        m=string.count(sub)
print(m)

    
