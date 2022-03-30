# print(".|.".center(24,"_"))
# print((".|."*3).center(24,"_"))
# print((".|."*5).center(24,"_"))
# print(("Welcme").center(24,"_"))
# print((".|."*5).center(24,"_"))
# print((".|."*3).center(24,"_"))
# print(".|.".center(24,"_"))
m,n=map(int,input().split())
thick=1
for i in range(m):
    for i in range(m//2):
        print((".|."*thick).center(n,"_"))
        thick+=2
    print(("Welcome").center(n,"_"))
    thick-=2
    break






