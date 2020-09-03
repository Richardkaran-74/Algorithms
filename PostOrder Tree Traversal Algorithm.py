class node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val
root = node(1)
root.childleft = node(2)
root.childright = node(3)
root.childleft.childleft = node(4)
root.childleft.childright = node(5)
#Inorder Tree Traversal Algorithm
def Postord(root):
    if root:
        Postord(root.childleft)
        Postord(root.childright)
        print(root.nodedata)
Postord(root)