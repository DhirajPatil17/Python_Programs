


class Mobile:
    __discount=50

    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def calculate(self):
        total=self.price-self.price*Mobile.__discount/100
        print("Your Phone of Brand ",self.brand, "Cost for ",self.price," by applying discount it will cost at :",total)


m1=Mobile("Apple",50000)
m2=Mobile("One Plus",40000)
m3=Mobile("Xiaomi",20000)
m4=Mobile("Vivo",25000)
m5=Mobile("Oppo",15000)

m1.calculate()



