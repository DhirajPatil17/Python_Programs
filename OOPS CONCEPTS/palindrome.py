str1="nitin"
count=0
high=len(str1)
mid=high//2
for i in range(0,mid):
    if str1[i]!=str1[len(str1)-(i+1)]:
        
        break
    else:
        count+=1
if count==mid:
    print("Palindrome")
else:
    print("  not a palindrome")


