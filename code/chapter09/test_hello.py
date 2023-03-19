import unittest
from hello import *

class SayHelloTestCase(unittest.TestCase): 
    
    def test_hello(self):
        result = say_hello("liu")
        self.assertEqual(result, 'hello liu')
        
    
if __name__ == '__main__':
    unittest.main()  


