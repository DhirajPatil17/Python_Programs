# splitting the multiline string into list 
s1="""he 
is 
very 
religious"""
print(s1.split('\n'))

# extract common values
s1="Python37"
s2="Python2.7"
s=''
for i in s1:
    if i in s2:
        s+=i
print(s)
# random item pick
import random

l1=['Red','Black','Blue','Green','White']
print(random.choice(l1))












