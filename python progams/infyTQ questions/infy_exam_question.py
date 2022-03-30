import itertools 
def palindrome(l1):
    l2=[]
    for i in l1:
        a=i[::-1]
        if a==i:
            if a not in l2:
                l2.append(int(a))
    print(max(l2))


innum=int(input())
c=str(innum)
num=list(c)
permutations=list(itertools.permutations(num))
l1=[''.join(permutations) for permutations in permutations]
palindrome(l1)

    




