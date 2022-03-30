class Patient:
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
        
    def calculate_bill_amount(self,consulation_fees,quantity_list,price_list):
        for list in range(len(quantity_list)):
            self.__bill_amount=quantity_list[list]*price_list[list]
            self.__bill_amount+=consulation_fees
        print(self.__bill_amount)
p1=Patient("Raunak",102)
p1.calculate_bill_amount(200,[1,2,3],[10,20,30])
p2=Patient("Dhiraj",103)
p2.calculate_bill_amount(300,[2,3,4],[23,30,20])


        