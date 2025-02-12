"""Rule 3"""

from .common import Common

class Rule010(Common):
    """Rule 3 processing"""

    @property
    def premises_rule_attrs(self):
        """Returns premises list"""
        if self.is_exception('building_name'):
            return ['name_and_thoroughfare_or_locality']
        if self.is_building_name_split_exception:
            return ['building_name_but_last_word', 'name_last_word_and_thoroughfare_or_locality']
        return ['building_name']

    @property
    def does_premises_include_first_thoroughfare_or_locality(self):
        """Returns if premises includes first thoroughfare or locality"""
        return self.is_exception('building_name') or self.is_building_name_split_exception

    @property
    def is_building_name_split_exception(self):
        """Returns if building name should be split"""
        return(
            self.is_exception('building_name_last_word') and
                not self.building_name_last_word.isdigit() and
                not self.is_exception_iv
            )

    @property
    def is_exception_iv(self):
        """Returns if building name starts with a known building type and
           ends with numeric range or numeric alpha suffix"""
        return (
            # Do not include suffix check as does not account for building names such as BLOCK B
            # re.match(r'^\d', self.building_name_last_word) and
                self.building_name_but_last_word in [
                    "BACK OF", "BLOCK", "BLOCKS", "BUILDING", "MAISONETTE", "MAISONETTES",
                    "REAR OF", "SHOP", "SHOPS", "STALL", "STALLS", "SUITE", "SUITES",
                    "UNIT", "UNITS"
                    ]
            )

    @property
    def building_name_last_word(self):
        """Returns last word of the building name"""
        *_, last = getattr(self, 'building_name', '').split()
        return last

    @property
    def building_name_but_last_word(self):
        """Returns all but last word of the building name"""
        *first, _ = getattr(self, 'building_name', '').split()
        return ' '.join(first)

    @property
    def name_last_word_and_thoroughfare_or_locality(self):
        """Returns last word of building name and first thoroughfare or locality"""
        return self._concatenate(['building_name_last_word', 'first_thoroughfare_or_locality'])
