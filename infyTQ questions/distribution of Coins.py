# def product(n1,n2,n3):
#     if(n1==7):
#         produc=n2*n3
#     elif n2==7:
#         produc=n3
#     elif n3==7:
#         produc=-1
#     else:
#         produc=n1*n2*n3
#     return produc



# num1=int(input("enter 1"))
# num2=int(input("enter 2"))
# num3=int(input("enter 3"))
# sol=product(num1,num2,num3)
# print(sol)
# def form_traingle(num1,num2,num3):
#     success="Yes traingle can be formed"
#     failure="No traingle cannot be formed"
#     if num3>=num1+num2 or num2>=num1+num3 or num1>=num2+num3:
#         return failure
#     else:
#         return success
# sol=form_traingle(1,7,3)
# print(sol)
def cost(money,five,one):
    no_of_five=0
    no_of_one=0
    total_five=five*5
    mol=money//5
    sum=0
    if total_five+one>=money:
        for i in range(1,total_five,5):
            while(no_of_five!=mol):
                if(sum!=money and sum<money and total_five!=0):
                    sum+=5
                    no_of_five+=1
                    total_five-=5
        for i in range(1,one):
            if(sum!=0 and sum<money and one!=0):
                sum+=1
                no_of_one+=1
                one-=1
        print("no_of_five",no_of_five)
        print("no_of_one",no_of_one)
    else:
        print(-1)
cost(49,12,6)

