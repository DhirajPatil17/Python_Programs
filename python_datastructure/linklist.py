class Node:
    def __init__(self,data):
        self.__data=data
        self.next=None
    def get_data(self):
        return self.__data
    def set_data(self,element):
        self.__data=element

class linklist:
    def __init__(self):
        self.head=None
    def printall(self):
        self.head=n1
        while self.head is not None:
            print(self.head.get_data(),end ="->")
            self.head=self.head.next
    def search(self,element):
        self.head=n1
        while(self.head is not None):
            if self.head.get_data()==element:
                print("element found")
                break
            elif self.head.get_data()!=element and self.head.next is None:
                print("element not found")
            self.head=self.head.next 
    def delete_at_end(self):
        self.head=n1
        while self.head is not None:
            if self.head.next is None:
                del self.head
                break
            print(self.head.get_data())
            self.head=self.head.next
    def insert_at_end(self,ele):
        self.head=n1
        while(self.head is not None):
            if self.head.next is None:
                self.head.set_data(ele)
                self.head.next=None
                break
            self.head=self.head.next
    def insert_at_begin(self,ele):
        new_node=Node(67)
        new_node.next=self.head
        self.head=new_node




n1=Node(10)
n2=Node(20)
n3=Node(46)
n4=Node(34)
n5=Node(25)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
l1=linklist()
l1.printall()
l1.search(89)
l1.insert_at_begin(92)
l1.delete_at_end()
l1.insert_at_end(33)
l1.printall()
l1.insert_at_begin(67)
l1.printall()
