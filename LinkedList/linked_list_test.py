from linked_list import LinkedList,Node

ll = LinkedList()
node1 = Node("data1",None) # tail
node2 = Node("data2",node1)
node3 = Node("data3",node2)
node4 = Node("data4",node3) # head

ll.head = node4
ll.insert_beginning("data_new")
ll.insert_last("last_new")
ll.insert_last("last_new_1")
ll.insert_last("last_new_2")


ll.print_ll()
data = ll.to_list()
print(data)
