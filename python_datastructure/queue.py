
class queue_imp:
    def __init__(self,size):
        self.__size=size
        self.__front=-1
        self.__rear=-1
        self.__arr=[]
    def isfull(self):
        if self.__front==0 and self.__rear==self.__size-1:
            return True
        else:
            return False
    def enqueue(self,ele):
        if self.isfull():
            print("queue is full")
        else:
            if len(self.__arr)==0:
                self.__arr.append(ele)
                self.__front+=1
                self.__rear+=1
            else:
                self.__arr.append(ele)
                self.__rear=+1
    def dequeue(self):
        if self.isempty:
            print("your queue is empty")
        elif self.__front==self.__rear:
            self.__arr.pop()
            self.__front=-1
            self.__rear=-1
        else:
            self.__arr.pop(0)
            self.__front+=1
        
    def isempty(self):
        if self.__front==-1 and self.__rear==-1:
            return True
        else:
            return False

    def print_queue(self):
        if self.isempty:
            print("your queue is empty")
        else:
            print("Your queue is:\n",self.__arr)
qu=queue_imp(4)
qu.enqueue(4)
qu.enqueue(6)
qu.enqueue(3)
qu.enqueue(9)
qu.enqueue(8)
qu.enqueue(17)
qu.print_queue()
qu.dequeue()
qu.print_queue()
qu.dequeue
qu.print_queue()
