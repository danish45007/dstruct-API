from linked_list import LinkedList
import unittest

class TestInsertMethod(unittest.TestCase):
    def test_inserting_at_beginning(self):
        print(f'********** Running Test For InsertAtBeginning Method **********')
        ll = LinkedList()
        ll.insert_beginning({"id":1})
        ll.insert_beginning({"id":2})
        ll.insert_beginning({"id":3})
        ll.insert_beginning({"id":4})
        ll.insert_beginning({"id":5})
        self.assertEqual(ll.to_list(),[{"id":5},{"id":4},{"id":3},{"id":2},{"id":1}])
    
    def test_inserting_at_last(self):
        print(f'********** Running Test For InsertAtLast Method **********')
        ll = LinkedList()
        ll.insert_last({"id":50})
        ll.insert_last({"id":40})
        ll.insert_last({"id":30})
        ll.insert_last({"id":20})
        ll.insert_last({"id":10})
        self.assertEqual(ll.to_list(),[{"id":10},{"id":20},{"id":30},{"id":40},{"id":50}])

class TestDeleteMethod(unittest.TestCase):
    def test_delete_by_id(self):
        print(f'********** Running Test For DeleteById Method **********')
        
        ll = LinkedList()
        ll.insert_beginning({"id":1})
        ll.insert_beginning({"id":2})
        ll.insert_beginning({"id":3})
        ll.insert_beginning({"id":4})
        ll.insert_beginning({"id":5})
        ll.delete_node_by_id(1)
        ll.delete_node_by_id(2)
        self.assertEqual(ll.to_list(),[{"id":5},{"id":4},{"id":3}])
