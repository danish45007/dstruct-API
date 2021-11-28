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
                
    def insert_data_from_file(self,path):
        with open(path,"r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line != "":
                    words = stripped_line.split()
                    for word in words:
                        self.level_order_insert(word)
                    
        
                
            
        