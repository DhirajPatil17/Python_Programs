class Mobile:
    discount=50
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    @staticmethod
    def set_discount(discount):
        Mobile.discount=discount
    def get_discount():
        return Mobile.discount
    def purchase(self):
        total=self.price-self.price*Mobile.discount/100
        print("Your phone brand is",self.brand,"cost at",self.price,"After applying discount amount is:",total)
s1=Mobile("Apple",23445)
s2=Mobile("Xiaomi",12313)
s3=Mobile("Vivo",32422)
print(Mobile.get_discount())
s1.purchase()

        