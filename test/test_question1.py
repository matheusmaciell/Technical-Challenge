import unittest
from src.question1 import Contracts,Contract

class TestStringMethods(unittest.TestCase):
    def setUp(self):
       self.contracts_obj = Contracts()
    
    def test_1 (self):
        """
        Test Base
        """
        contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5)]

        renegotiated = [3]
        top_n = 3

        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [5, 4, 2]
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')

    def test_2(self):
        """
        Test 2
        """
        contracts = [
        Contract(1, 10),
        Contract(2, 9),
        Contract(3, 9),
        Contract(4, 8),
        Contract(5, 7)]

        renegotiated = [3,2]
        top_n = 3
        
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [1, 4, 5]
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')

    def test_3(self):
        """
        Test 3
        """
        contracts = [
        Contract(1, 10),
        Contract(2, 9),
        Contract(3, 9),
        Contract(4, 8),
        Contract(5, 11)]

        renegotiated = [3,2]
        top_n = 4

        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [5, 1, 4]
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')

    def test_4(self):
        """
        Test 4
        """
        contracts = [
        Contract(1, 10),
        Contract(2, 9),
        Contract(3, 9),
        Contract(4, 8),
        Contract(5, 11)]

        renegotiated = [3,2]
        top_n = 1

        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [5]
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')
    def test_5(self):
        """
        Test 5
        """
        contracts = [
        Contract(1, 10),
        Contract(2, 9),
        Contract(3, 9),
        Contract(4, 8),
        Contract(5, 11)]

        renegotiated = [1,3,2,4,5]
        top_n = 1

        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = []
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')
    def test_6(self):
        """
        Test 6
        """
        contracts = [
        Contract(1, 10),
        Contract(2, 9),
        Contract(3, 9),
        Contract(4, 8),
        Contract(5, 11)]

        renegotiated = []
        top_n = 4

        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [5,1,2,3]
        self.assertEqual(expected_open_contracts, actual_open_contracts, 'should be equal')
    def test_7(self):
        """
        Test 7
        """
        contracts = [
            Contract(1, 3),
            Contract(2, 5),
            Contract(3, 66),
            Contract(6, 7),
            Contract(5, 15),
            Contract(4, 10)
        ]
        renegotiated = [3]
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )
        expected_open_contracts = [5, 4, 6]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')
    
    def test_8(self):
        """
        Test 8
        """
        contracts = [
            Contract(1, 3),
            Contract(2, 5),
            Contract(3, 66),
            Contract(6, 7),
            Contract(5, 15),
            Contract(4, 10)
        ]
        renegotiated = []
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )
        expected_open_contracts = [3, 5, 4]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')

    def test_9(self):
        """
        Test 9
        """
        contracts = [
            Contract(1, 3),
            Contract(2, 5),
            Contract(3, 66),
            Contract(6, 7),
            Contract(5, 15),
            Contract(4, 10)
        ]
        renegotiated = [1, 2, 3, 4, 5, 6]
        top_n = 3
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )
        expected_open_contracts = []
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')

    def test_10(self):
        """
        Test 10
        """
        contracts = [
            Contract(1, 3),
            Contract(2, 5),
            Contract(3, 66),
            Contract(6, 7),
            Contract(5, 15),
            Contract(4, 10)
        ]
        renegotiated = [4, 5, 1]
        top_n = 10000
        actual_open_contracts = self.contracts_obj.get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )
        expected_open_contracts = [3, 6, 2]
        self.assertEqual(actual_open_contracts, expected_open_contracts, 'should be equal')
if __name__ == '__main__':
    unittest.main()