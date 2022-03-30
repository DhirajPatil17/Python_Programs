from math import sqrt
def primeno(n):
    p=[]

    for num in range(0, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                p.append(num)
    return p                        

def isprime(n):
    prime_flag = 0
  
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
from datetime import timedelta, date

l={'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6,'sat':7}
k={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
h={'01':1,'02':2,'03':3,'04':4,'05':5,'06':6,'07':7,'08':8,'09':9,'10':10,'11':11,'12':12}
primemo=['02','02','05','07','11']


n=100
s=[]
for i in primeno(n):
    Date_required = date.p + timedelta(days=i)
    jk=str(Date_required).split('-')
    ll=jk[1]
    if isprime(h[ll]):
        s.append(i)

print(s)        

    

