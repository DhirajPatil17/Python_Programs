class StackImpl:
    def __init__(self,size):
        self.__capacity=size
        self.__list=[]
    def isEmpty(self): #this function is to check the current size of the list before inserting
        if len(self.__list)<self.__capacity:
            return True
        else:
            return False
    def isavaliable(self):# this function is to check weather item is available in list or not before popping it
        if len(self.__list)==0:
            return True
        else:
            return False 

    def push(self,data): # this function is to insert data into the list
        if self.isEmpty():
            self.__list.append(data)
            print("Inserted")
        else:
            print("Stack is full")
    def pop(self):# this function is for pop operation
        if self.isavaliable():
            print("List is empty")
        else:
            self.__list.pop()
            print("Item popped") 
    def getvalue(self): # this is the function to print the entire list
        print("Your entire list",self.__list)
ob=StackImpl(5)
while(ob.isEmpty()):
    ob.push(int(input()))
ob.getvalue()
ob.pop()
ob.getvalue()



        