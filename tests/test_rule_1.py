"""Test Address Rule 1 formatting"""

import unittest
import paf

class TestRule1(unittest.TestCase):
    """Test Address Rule 1"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'organisation_name': "LEDA ENGINEERING LTD",
            'dependent_locality': "APPLEFORD",
            'post_town': "ABINGDON",
            'postcode': "OX14 4PG"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["LEDA ENGINEERING LTD", "APPLEFORD", "ABINGDON", "OX14 4PG"]
        self.assertEqual(self.address.list(), address, "Incorrect Rule 1 list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "LEDA ENGINEERING LTD, APPLEFORD, ABINGDON. OX14 4PG"
        self.assertEqual(self.address.str(), address, "Incorrect Rule 1 string format")

if __name__ == '__main__':
    unittest.main()
