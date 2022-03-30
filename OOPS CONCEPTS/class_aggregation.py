#class aggregation
class Customer:
    def __init__(self,name,salary,age,address):
        self.name=name
        self.salary=salary
        self.age=age
        self.address=address
    def show_details(self):
        print("Customer Details:\n Customer name is:{}\n salary is:{}\n age is:{}\n".format(self.name,self.salary,self.age))
        print("Customers Address:\n Door:{}\n Street:{}\n Pincode:{}".format(self.address.door,self.address.street,self.address.pincode))
class Address:
    def __init__(self,door,street,pincode):
        self.door=door
        self.street=street
        self.pincode=pincode
Add1=Address(123,"5th lane",56001)
Add2=Address(567,"6th lane",82006)

    
        
c1=Customer("Dhiraj",500000,21,Add1)
c2=Customer("Vinod",1000000,45,Add2)
c1.show_details()
c2.show_details()