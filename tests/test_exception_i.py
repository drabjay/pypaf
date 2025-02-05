"""Test Address Exception I formatting"""

import unittest
import paf

class TestExceptionI(unittest.TestCase):
    """Test Address Exception I"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'building_name': "1-2",
            'thoroughfare_name': "NURSERY",
            'thoroughfare_descriptor': "LANE",
            'dependent_locality': "PENN",
            'post_town': "HIGH WYCOMBE",
            'postcode': "HP10 8LS"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["1-2 NURSERY LANE", "PENN", "HIGH WYCOMBE", "HP10 8LS"]
        self.assertEqual(self.address.list(), address, "Incorrect Exception I list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "1-2 NURSERY LANE, PENN, HIGH WYCOMBE. HP10 8LS"
        self.assertEqual(self.address.str(), address, "Incorrect Exception I string format")

if __name__ == '__main__':
    unittest.main()
