class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def to_list(self):
        data_list = []
        node = self.head
        if node is None:
            return data_list
        while node:
            data_list.append(node.data)
            node = node.next_node    
        return data_list
    
    def print_ll(self):
        ll_string = ""
        head = self.head
        if head == None:
            print(None)
        while head:
            ll_string += f" {str(head.data)} ->"
            head = head.next_node
        ll_string += " None"
        print(ll_string)
        
    def insert_beginning(self,data):
        new_head_node = Node(data,next_node=self.head)
        self.head = new_head_node
    
    def insert_last(self,data):
        if self.head is None:
            self.insert_beginning(data)
        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = Node(data,None)
            self.last_node = node.next_node
        else:
            self.last_node.next_node = Node(data,None)
            self.last_node = self.last_node.next_node

    def get_node_by_id(self,id):
        node = self.head
        while node:
            if node.data["id"] == int(id):
                return node.data
            node = node.next_node
        return None
    
    def delete_node_by_id(self,id):
        node = self.head
        while node:
            if node.next_node.data["id"] == int(id):
                node.next_node = node.next_node.next_node
                return node
            node = node.next_node
        return None
                
            




