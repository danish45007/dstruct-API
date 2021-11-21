from qqueue import Queue
import unittest

class TestQueuesMethods(unittest.TestCase):
    def test_enqueue_method(self):
        print(f'********** Running Test For Enqueue Method **********')
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        output = q.to_list()
        expected_output = [1,2,3]
        self.assertListEqual(output,expected_output)
        self.assertNotEqual(output,[1,1])
       
    def test_denqueue_method(self):
        print(f'********** Running Test For Denqueue Method **********')
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        output_1 = q.dequeue()
        output_2 = q.dequeue()
        output_3 = q.dequeue()
        self.assertEqual(output_1.data,1)
        self.assertEqual(output_2.data,2)      
        self.assertEqual(output_3.data,3)
        self.assertNotEqual(output_1.data,2)
        self.assertNotEqual(output_2.data,3)      
        self.assertNotEqual(output_3.data,4)      
              
  
        