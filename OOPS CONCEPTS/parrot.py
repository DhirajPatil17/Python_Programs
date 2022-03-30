class Parrot:
    __counter=7000
    def __init__(self):
        Parrot.__counter+=1
        self.__name=None
        self.__beak_color=None
        self.__unique_number=Parrot.__counter
        
    
    
    def get_name(self):
        return self.__name
    def get_beak_color(self):
        return self.__beak_color
    def get_unique_number(self):
        return self.__unique_number
    
    