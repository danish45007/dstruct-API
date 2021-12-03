from data_structure.node import Node
from data_structure.queue_ import Queue

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def level_order_insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        
        q = Queue()
        q.enqueue(self.root)
        # while queue not empty
        while q.get_len():
            node = q.dequeue()
            if not node.left:
                node.left = Node(data)
                return
            else:
                q.enqueue(node.left)
            if not node.right:
                node.right = Node(data)
                return
            else:
                q.enqueue(node.right)
                
    def bst_insert_recursive(self,data,node):
        
        if int(data) < int(node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self.bst_insert_recursive(data,node.left)
        elif int(data) > int(node.data):
            if node.right is None:
                node.right = Node(data)
            else:
                self.bst_insert_recursive(data,node.right)
        else:
            return
    
    def bst_insert(self,data): 
        if self.root is None:
            self.root = Node(data)
            return
        else:
            self.bst_insert_recursive(data,self.root)
                
    def insert_data_from_file(self,path):
        with open(path,"r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line != "":
                    words = stripped_line.split()
                    for word in words:
                        self.level_order_insert(word)
    
    def insert_data_from_file_for_bst(self,path):
        with open(path,"r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line != "":
                    words = stripped_line.split()
                    for word in words:
                        self.bst_insert(word)
                        
    
                    
        
                
            
        