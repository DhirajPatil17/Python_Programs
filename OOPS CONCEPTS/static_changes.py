class Mobile:
    discount=50
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand
    def purchase(self):
        total=self.price-self.price*Mobile.discount/100

        print("Your brand is",self.brand,"Cost at",self.price,"After applying discount: ",total)
def enable_discount():
    Mobile.discount=50
def disable_discount():
    Mobile.discount=0
m1=Mobile(10000,"Apple")
m2=Mobile(25000,"Xiaomi")
m3=Mobile(30000,"Vivo")
m4=Mobile(45000,"One Plus")
enable_discount()
m1.purchase()
m2.purchase()
disable_discount()
m3.purchase()
m4.purchase()






        