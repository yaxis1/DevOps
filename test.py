from flask import Flask, request
import unittest, requests

class FlaskTest(unittest.TestCase):
    url = 'http://localhost:5000/'

    def test_1_home(self):
        r = requests.get(FlaskTest.url)
        self.assertEqual(r.status_code, 200)

  
    def test_2_send(self):
        # Test function for multiples of 7
    
        #     assert multiples_of_7(7) == [7]
        #     assert multiples_of_7(14) == [7, 14]
        #     assert multiples_of_7(21) == [7, 14, 21]
        #     assert multiples_of_7(28) == [7, 14, 21, 28]
        #     assert multiples_of_7(35) == [7, 14, 21, 28, 35]
        #     assert multiples_of_7(42) == [7, 14, 21, 28, 35, 42]
        r = requests.post(FlaskTest.url+'/send', data = {'num1':1, 'num2':2, 'multiple_num' : 5, 'text': 'test', 'com_num': 1})
    #    r.
        #self.assertTrue(b'That username is already taken!' in r.content) 

if __name__ == '__main__':
    unittest.main()

