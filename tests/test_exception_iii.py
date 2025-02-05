"""Test Address Exception III formatting"""

import unittest
import paf

class TestExceptionIII(unittest.TestCase):
    """Test Address Exception III"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'building_name': "K",
            'thoroughfare_name': "PORTLAND",
            'thoroughfare_descriptor': "ROAD",
            'post_town': "DORKING",
            'postcode': "RH4 1EW"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["K PORTLAND ROAD", "DORKING", "RH4 1EW"]
        self.assertEqual(self.address.list(), address, "Incorrect Exception III list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "K PORTLAND ROAD, DORKING. RH4 1EW"
        self.assertEqual(self.address.str(), address, "Incorrect Exception III string format")

if __name__ == '__main__':
    unittest.main()
