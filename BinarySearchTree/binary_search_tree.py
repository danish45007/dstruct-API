class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None,
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def _insert_recursive(self,data,node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data,node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data,node.right)
        else:
            return
                
    def insert_data(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data,self.root)
            
    def _search_recursive(self,id,node):
        if node.left == None and node.right == None:
            return False
        if id == node.data["id"]:
            return node.data
        # search in the left node
        if id < node.data["id"] and id == node.left.data["id"]:
            return node.left.data
        else:
            self._search_recursive(id,node.left)
        # search in right node
        if id > node.data["id"] and id == node.right.data["id"]:
            return node.right.data
        else:
            self._search_recursive(id,node.right)
                   
    def search(self,id):
        _id = int(id)
        if self.root is None:
            return False
        return self._search_recursive(_id,self.root)