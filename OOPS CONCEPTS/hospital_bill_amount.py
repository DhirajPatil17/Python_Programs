class Bill:
    def __init__(self,patient_name,bill_id):

        self.__patient_name=patient_name
        self.__bill_id=bill_id
        self.__bill_amount=0
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        for i in range(len(quantity_list)):
            self.__bill_amount+=quantity_list[i]*price_list[i]
        self.__bill_amount+=consultation_fees
        return self.get_bill_amount()
b1=Bill("Sanket",125)
print(b1.calculate_bill_amount(50,[6,4,2],[100,150,100]))
b1=Bill("Dhiraj",789)
print(b1.calculate_bill_amount(20,[1,2,4],[50,100,150]))

        
        

        