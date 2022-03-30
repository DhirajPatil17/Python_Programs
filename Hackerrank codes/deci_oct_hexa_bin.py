# num=int(input())
# for i in range(1,num+1):
#     print("{} {} {} {}".format(i,oct(i),hex(i),bin(i)))
# n = int(input())
# width = len("{0:b}".format(n))
# print(width)
# for i in range(1,n+1):
#   print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
def print_formatted(number):
    width=len("{0:b}".format(number))
    
    for i in range(1,number+1):
        print("{0:{width}d}  {0:{width}o}  {0:{width}X} {0:{width}b}".format(i,width=width))
 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)