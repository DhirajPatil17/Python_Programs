
# To print the average of the list items using functions
l1=[1,2,3,4,5]
def average(l1):
    """
    generate values for the average
    >>> print(average(l1))
    2.0
    >>> print(average([1,2,3,4]))
    5.0
    >>> print(average([1,2,3,4]))
    5.0
    """
    s=sum(l1)
    avg=s/len(l1)
    return avg
print(average(l1))

print("vampire diaries.".title())
print("s".upper())
print(chr(122))#for ascii alphabets.
print(ord("b"))# for ascii values
# Converting the word into the capitalise form 
def to_upper(s):
    c=ord(s)
    if c in range(97,123):
        return chr(ord(s)-32)
    else:
        return s
print(to_upper("b"))
def capitalize(st):
    return to_upper(st[0])+st[1:]
print(capitalize("dhiraj patil"))
# checking the ascii values of the character entered print yes if true or or flase if no
def is_digit(ch):
    status=True
    for i in ch:
        a=ord(i)
        if a not in range(48,58):
            status=False
            break
    if status == False:
        print("Not")
    else:
        print("Yes")
is_digit("1234")# only digits are considered and .points are not considered as digits

# count the character which occurs only once
s = "geeks for geeks"

d = {}

for i in s:
    count = s.count(i)
    if count ==1:
        print(i)
# Reverse the string using split function
inp="Do or ,die how much harder you try."

c=list(inp.split())
l1=[]
for i in c[::-1]:
    l1.append(i)
print(" ".join(l1))
a=''






