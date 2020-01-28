class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+"Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+"Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+" is Found")
    def inorderTraversal(self,root):
            res = []
            if root:
                res = self.inorderTraversal(root.left)
                res.append(root.data)
                res = res + self.inorderTraversal(root.right)
            return res
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    def PostorderTrraversal(self,root):
        res = []
        if root:
            res = self.PostorderTrraversal(root.left)
            res = res+self.PostorderTrraversal(root.right)
            res.append(root.data)
        return res
    def deleltion(self,num):
        if num < self.data:
            if self.left is None:
                return str(num)+"Not Found"
            elif self.right.data == num:
                self.right = None
                return True
            elif self.left.data == num:
                self.left = None
                return True
            return self.left.deleltion(num)
        elif num > self.data:
            #x = self.right
            #print(x)
            #print("X")
            #print(self.right.data)
            if self.right is None:
                return str(num)+"Not Found"
            #else:
                #self.right = None
                #return True
            elif  self.right.data == num:
                self.right = None
                #print(self.right.data)
                return True
            elif self.left.data == num:
                self.left = None
                return True
            return self.right.deleltion(num)
        else:
            if self.left is None and self.right is None:
                pass
            
    
root = Node(100)
root.insert(50)
root.insert(60)
root.insert(30)
root.insert(150)
root.insert(120)
root.deleltion(120)
print(root.inorderTraversal(root))
#print(root.PreorderTraversal(root))
#print(root.PostorderTrraversal(root))
#for i in range(51):
    #root.insert(i)
root.PrintTree()
#print(root.findval(56))

