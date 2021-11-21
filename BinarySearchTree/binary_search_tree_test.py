from binary_search_tree import BinarySearchTree
import unittest

class TestSearchMethodOnBST(unittest.TestCase):
    def test_search_by_id(self):
        print(f'********** Running Test For SearchById Method **********')
        test_data = [
			{
				"id": 1,
				"val": 100,
			},
			{
				"id": 2,
				"val": 200
			},
			{
				"id": 3,
				"val": 300
			}
			
		]
        bst = BinarySearchTree()
        for data in test_data:
            bst.insert(data)
        # Test Cases
        # +ve test cases
        self.assertEqual(bst.search(1)["val"],100)
        self.assertEqual(bst.search(2)["val"],200)
        self.assertEqual(bst.search(3)["val"],300)
        
        # -ve test cases
        self.assertNotEqual(bst.search(1)["val"],200)
        self.assertNotEqual(bst.search(2)["val"],300)
        self.assertNotEqual(bst.search(3)["val"],600)
        


