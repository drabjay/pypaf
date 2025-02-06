"""Test Address PO Box formatting"""

import unittest
import paf

class TestPoBox(unittest.TestCase):
    """Test Address PO Box"""

    def setUp(self):
        """Set up Address instance"""
        self.address = paf.Address({
            'po_box_number': "61",
            'post_town': "FAREHAM",
            'postcode': "PO14 1UX"
            })

    def test_list(self):
        """Test conversion to an list"""
        address = ["PO BOX 61", "FAREHAM", "PO14 1UX"]
        self.assertEqual(self.address.as_list(), address, "Incorrect PO Box list format")

    def test_string(self):
        """Test conversion to a string"""
        address = "PO BOX 61, FAREHAM. PO14 1UX"
        self.assertEqual(self.address.as_str(), address, "Incorrect PO Box string format")

    def test_tuple(self):
        """Test conversion to a tuple"""
        address = ("PO BOX 61", "FAREHAM", "PO14 1UX")
        self.assertEqual(self.address.as_tuple(), address, "Incorrect PO Box tuple format")

    def test_dict(self):
        """Test conversion to a dict"""
        address = {'line_1': "PO BOX 61", 'post_town': "FAREHAM", 'postcode': "PO14 1UX"}
        self.assertEqual(self.address.as_dict(), address, "Incorrect PO Box dict format")

if __name__ == '__main__':
    unittest.main()
