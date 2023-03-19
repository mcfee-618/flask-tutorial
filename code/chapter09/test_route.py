import unittest
from app import *

class AppTestCase(unittest.TestCase): 
    
    def setUp(self):
        self.client = app.test_client() 
        print(222)
        
    def login(self):
        self.client.post('/login', data=dict(
            username='fei',
            password='123'
        ))
    
    def test_hello(self):
        self.login()
        response = self.client.get('/index')  # 传入目标 URL
        data = response.get_data(as_text=True)
        print(data)
       
        
    
if __name__ == '__main__':
    unittest.main()  
