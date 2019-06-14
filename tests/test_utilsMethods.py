import unittest
import Utils

class TestUtilsMethods(unittest.TestCase):

    def test_get_hello_world(self):        
        self.assertEqual(Utils.get_hello_world(), 'hello world')

if __name__ == '__main__':
    unittest.main()