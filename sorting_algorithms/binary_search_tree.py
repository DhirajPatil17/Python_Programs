class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        if self.key==data:
            return
        if self.key >data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present") 
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key,end=" ")
    # def delete(self,data):
    #     if self.key is None:
    #         print("tree is empty")
    #         return
    #     if data<self.key:
    #         if self.lchild:
    #             self.lchild=self.lchild.delete(data)
    #         else:
    #             print("data is not present in the tree")
    #     elif data>self.key:
    #         if self.rchild:
    #             self.rchild=self.rchild.delete(data)
    #         else:
    #             print("data is not present in the tree")
    #     else:
    #         if self.lchild is None:
    #             temp=self.rchild
    #             self=None
    #             return None
    #         if self.rchild is None:
    #             temp=self.lchild
    #             self=None
    #             return None
root=BST(19)
l1=[6,3,1,98,13,7]
for i in l1:
    root.insert(i)

root.search(98)
print("pre order")
root.preorder()
print("postorder")
root.postorder()
print("inorder")
root.inorder()
root.delete(3)