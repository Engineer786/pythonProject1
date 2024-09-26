import unittest
from test_code1 import circle_area
class TestClassDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution...')
    def setUp(self):
        print('setUp method execution...')
    def test_circle_area(self):
       r = [2, 4, 0]
       for r1 in r:
           a = circle_area(r1)
           return a
    # def test_method2(self):
    #     print('test method2 execution...')
    def tearDown(self):
        print('tearDown method execution...')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method execution...')

if __name__ == '__main__':
     unittest.main()

