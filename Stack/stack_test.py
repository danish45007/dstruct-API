from stack import Stack
import unittest

class TestPeekMethod(unittest.TestCase):
    """
        returns the top element from the stack
    """
    def test_stack_peek(self):
        print(f'********** Running Test For Peek Method **********')
        stk = Stack()
        stk.push(1)
        stk.push(2)
        stk.push(3)
        stk.push(4)
        output_node = stk.peek()
        self.assertEqual(output_node.data,4)
        
class TestPopMethod(unittest.TestCase):
    """
        removes the top element from the stack and returns it
    """
    def test_stack_pop(self):
        print(f'********** Running Test For Pop Method **********')
        stk = Stack()
        stk.push(1)
        stk.push(2)
        stk.push(3)
        stk.push(4)
        removed_node_1 = stk.pop()
        removed_node_2 = stk.pop()
        removed_node_3 = stk.pop()
        removed_node_4 = stk.pop()
        # +ve test cases
        self.assertEqual(removed_node_1.data,4)
        self.assertEqual(removed_node_2.data,3)
        self.assertEqual(removed_node_3.data,2)
        self.assertEqual(removed_node_4.data,1)
        # -ve test cases
        self.assertNotEqual(removed_node_1.data,40)
        self.assertNotEqual(removed_node_2.data,30)
        self.assertNotEqual(removed_node_3.data,20)
        self.assertNotEqual(removed_node_4.data,10)
        