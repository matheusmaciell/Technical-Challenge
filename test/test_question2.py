import unittest
from src.question2 import Orders

class TestStringMethods2(unittest.TestCase):
    
    def setUp(self):
        self.orders_obj = Orders()
    
    def test_1 (self):
        """
        Test Base
        """
        orders = [70, 30, 10]
        n_max = 100
        expected_orders = 2

        how_many = self.orders_obj.combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders, 'should be equal')
    def test_2 (self):
        """
        Test 2
        """
        orders = [70, 70, 70]
        n_max = 100
        expected_orders = 3

        how_many = self.orders_obj.combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders, 'should be equal')

    def test_3 (self):
        """
        Test 3
        """
        orders = [100, 1, 70]
        n_max = 100
        expected_orders = 2

        how_many = self.orders_obj.combine_orders(orders, n_max)
    
        self.assertEqual(how_many, expected_orders, 'should be equal')    
    def test_4 (self):
        """
        Test 4
        """
        orders = [1, 1, 70]
        n_max = 100
        expected_orders = 2

        how_many = self.orders_obj.combine_orders(orders, n_max,)

        self.assertEqual(how_many, expected_orders, 'should be equal')
    def test_5 (self):
        """
        Test 5
        """
        orders = [1, 1, 70,1,1,99,70]
        n_max = 100
        expected_orders = 4

        how_many = self.orders_obj.combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders, 'should be equal') 
    def test_6 (self):
        """
        Test 6
        """
        orders = [1, 1, 2,3,1,1,1]
        n_max = 5
        expected_orders = 4

        how_many = self.orders_obj.combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders, 'should be equal') 
    def test_7 (self):
        """
        Test 4
        """
        orders = [1, 1, 2,3,1,1,1]
        n_max = 5
        expected_orders = 4

        how_many = self.orders_obj.combine_orders(orders, n_max)

        self.assertEqual(how_many, expected_orders, 'should be equal')


    def test_8(self):
        """
        Test 8
        """
        orders = [30, 80, 15, 1, 100, 70, 50, 50]
        n_max = 100
        how_many = self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 6
        self.assertEqual(how_many, expected_orders, 'should be equal')

    def test_9(self):
        """
        Test 9
        """
        orders = [30, 80, 15, 1, 100, 70, 50, 50]
        n_max = 200
        how_many =  self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 4
        self.assertEqual(how_many, expected_orders, 'should be equal')

    def test_10(self):
        """
        Test 10
        """
        orders = [30, 80, 15, 80, 70, 70, 50, 50]
        n_max = 80
        how_many =  self.orders_obj.combine_orders(orders, n_max)
        expected_orders = 8
        self.assertEqual(how_many, expected_orders, 'should be equal')  


if __name__ == '__main__':
    unittest.main()        