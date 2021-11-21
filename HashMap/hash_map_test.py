from hash_map import HashTable
import unittest


class TestAddKeyValuePair(unittest.TestCase):
    def test_string_key_numeric_value(self):
        print(f'********** Running Test For AddKeyValuePair Method **********')
        ht = HashTable(5)
        ht.add_key_value_pair("test",1)
        ht.add_key_value_pair("test",2)
        ht.add_key_value_pair("test1",3)
        expected_result = '\n\t\t{\n    \t\t[0] test1 : 3\n    \t\t[[100 chars]    ' != '{    [0] test1 : 3    [1] test : 1 --> te[48 chars]one}'
        output = ht.print_table()
        self.assertEqual(str(expected_result),str(output))
        
        
class TestGetValueByKey(unittest.TestCase):
    def test_get_value_key_key(self):
        print(f'********** Running Test For GetValueByKey Method **********')
        ht = HashTable(5)
        ht.add_key_value_pair("test","abc")
        ht.add_key_value_pair("test","cde")
        ht.add_key_value_pair("test1","pop")
        ht.add_key_value_pair("test2",3)
        ht.add_key_value_pair("test3",4)
        expected_result_1 = ht.get_value("test")
        expected_result_2 = ht.get_value("test1")
        expected_result_3 = ht.get_value("test2")
        expected_result_4 = ht.get_value("test3")
        # expected_result_5 = ht.get_value("test")
        self.assertEqual(expected_result_1,"abc")
        self.assertEqual(expected_result_2,"pop")
        self.assertEqual(expected_result_3,3)
        self.assertEqual(expected_result_4,4)
        # self.assertEqual(expected_result_5,"cde")
        
        
        
    