


class Customer:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone_no=phone
    def purchase(self,payment):
        print("Customer info:\n Name:{} \n age:{} \n phone:{}".format(self.name,self.age,self.phone_no))
        if payment.type=="card":
            print("Payment done by Card")
        elif payment.type=="e-wallet":
            print("Payment done by wallet")
        else:
            print("Payment by cash")
        
class Payment:
    def __init__(self,type):
        self.type=type
p1=Payment("card")
c1=Customer("Aaryan",60,12345)
c1.purchase(p1)
        
        