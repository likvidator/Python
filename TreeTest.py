class Tree:
    def __init__(self):
        self.root = None

    


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def add_left(self,node):
        self.left=node
        node.parent = self
        

    def add_right(self,node):
        self.right=node
        node.parent = self

    def __repr__(self):
        return "<Node, value=%s>" % self.value
        

    def subtree(self, ntabs = 0):
        for i in range(ntabs):
            print "\t",
        print self.value
        
        if self.left != None:
            self.left.subtree(ntabs + 1)
        if self.right != None:
            self.right.subtree(ntabs + 1)

    def print_for_graphviz(self):
        
        if self.parent == None:
            parent_value = None
        else:
            parent_value = self.parent.value
            
        print parent_value, "->", self.value
        
        if self.left != None:
            self.left.print_for_graphviz()
        if self.right != None:
            self.right.print_for_graphviz()

    def add_value(self,node):
        if node.value>self.value:
            if self.right==None:
                self.add_right(node)
            else:
                self.right.add_value(node)
        if node.value<self.value:
            if self.left==None:
                self.add_left(node)
            else:
                self.left.add_value(node)

    
    def write_for_graphviz(self,f):
            
            if self.parent == None:
                parent_value = None
            else:
                parent_value = self.parent.value
            
            f.write(str(parent_value))
            f.write("->")
            f.write(str(self.value))
            f.write('\n')
        
            if self.left != None:
                self.left.write_for_graphviz(f)
            if self.right != None:
                self.right.write_for_graphviz(f)
                
    def write_file(self):
        f=open('tree.txt','w')
        f.write("digraph G{ ")
        self.write_for_graphviz(f)
        f.write("}")
        f.close()


    def delete_branch(self, value):
       if self.value == value:
           if self.parent != None:
               if self.value > self.parent.value:
                   self.parent.right = None
               else:
                   self.parent.left = None
               if self.right != None:
                   self.parent.add_value(self.right)
               if self.left != None:
                   self.parent.add_value(self.left)
       else:
         if self.left != None:
            self.left.delete_branch(value)
         if self.right != None:
             self.right.delete_branch(value)
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""#
#_______________________________________________________________________#
n=input("Length=")
z=[]
a=0
while a<n:
    x=input("a=")
    z=z+[x]
    a+=1
a=0
n1=Node(z[0])
while a<len(z)-1:
    a+=1
    n1.add_value(Node(z[a]))


