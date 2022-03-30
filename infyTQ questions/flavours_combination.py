
import math
def find_number_of_combination(number_of_flavours):
    total_combinations=0
    
        
    total_combinations=pow(2,number_of_flavours)
    return total_combinations
    

    

number_of_combination=find_number_of_combination(6)
print(number_of_combination)
import math
def find_number_of_combination(number_of_flavours):
    total_combinations=0
    
        
    total_combinations=math.factorial(number_of_flavours)
    return total_combinations
    

    

number_of_combination=find_number_of_combination(6)
print(number_of_combination)