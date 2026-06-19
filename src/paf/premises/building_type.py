"""Building Types"""

from .split import SplitMixin


class BuildingTypeMixin(SplitMixin):
    """Determines if a string represents a known building type"""

    known_building_types = (
        "BACK OF", "BLOCK", "BLOCKS", "BUILDING",
        "MAISONETTE", "MAISONETTES", "REAR OF",
        "SHOP", "SHOPS", "STALL", "STALLS",
        "SUITE", "SUITES", "UNIT", "UNITS",
        "FLAT", "FLATS", "PO BOX"
        )
    known_sub_building_types = known_building_types
    known_split_building_types = ("UNIT",)

    def is_known_building_type(self, attr='building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_building_types

    def is_known_sub_building_type(self, attr='sub_building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_sub_building_types

    def is_known_split_building_type(self, attr='building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_split_building_types
