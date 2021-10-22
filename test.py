from src3 import app
import unittest, requests


class FlaskTest(unittest.TestCase):
    url = 'http://localhost:2022/'

    def test_1_home(self):
        with app.app_context(): 
            r = requests.get(FlaskTest.url+'/' )
            self.assertEqual(r.status_code, 200)

    def test_2_send(self):
        #Check if returns text
        r = requests.post(FlaskTest.url+'/send' , data = {'num1': 1, 'num2':20, 'multiple_num' : 1, 'text': 'value', 'com_num': 1})
        return 'value' in r.content.decode('utf-8')

    def test_3_send(self):
        #Check if returns string of multiples 
        r = requests.post(FlaskTest.url+'/send' , data = {'num1': 1, 'num2':20, 'multiple_num' : 7, 'text': 'value', 'com_num': 3})
        return '[7, 14]' in r.content.decode('utf-8')
         
 
if __name__ == '__main__':
    unittest.main()

