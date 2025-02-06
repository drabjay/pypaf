"""Test Address Rule 4 formatting"""

import unittest
import paf

class TestRule4(unittest.TestCase):
    """Test Address Rule 4"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'building_name': "VICTORIA HOUSE",
            'building_number': "15",
            'thoroughfare_name': "THE",
            'thoroughfare_descriptor': "STREET",
            'post_town': "CHRISTCHURCH",
            'postcode': "BH23 6AA"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["VICTORIA HOUSE", "15 THE STREET", "CHRISTCHURCH", "BH23 6AA"]
        self.assertEqual(self.address.as_list(), address, "Incorrect Rule 4 list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "VICTORIA HOUSE, 15 THE STREET, CHRISTCHURCH. BH23 6AA"
        self.assertEqual(self.address.as_str(), address, "Incorrect Rule 4 string format")

    def test_tuple(self):
        """Test conversion to a tuple"""
        address = ("VICTORIA HOUSE", "15 THE STREET", "CHRISTCHURCH", "BH23 6AA")
        self.assertEqual(self.address.as_tuple(), address, "Incorrect Rule 4 tuple format")

if __name__ == '__main__':
    unittest.main()
