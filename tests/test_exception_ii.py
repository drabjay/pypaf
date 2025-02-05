"""Test Address Exception II formatting"""

import unittest
import paf

class TestExceptionII(unittest.TestCase):
    """Test Address Exception II"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'building_name': "12A",
            'thoroughfare_name': "UPPERKIRKGATE",
            'post_town': "ABERDEEN",
            'postcode': "AB10 1BA"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["12A UPPERKIRKGATE", "ABERDEEN", "AB10 1BA"]
        self.assertEqual(self.address.list(), address, "Incorrect Exception II list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "12A UPPERKIRKGATE, ABERDEEN. AB10 1BA"
        self.assertEqual(self.address.str(), address, "Incorrect Exception II string format")

if __name__ == '__main__':
    unittest.main()
