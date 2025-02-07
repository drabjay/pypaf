"""Common"""

import re

class Common:
    """Common premises processing"""

    @property
    def premises_rule_attrs(self):
        """Abstract method to be implemented by the Rule"""

    @property
    def premises(self):
        """Returns premises list"""
        return [getattr(self, k) for k in self.premises_rule_attrs]

    @property
    def name_and_thoroughfare_or_locality(self):
        """Returns building number and first thoroughfare or locality"""
        return self._concatenate(['building_name', 'first_thoroughfare_or_locality'])

    @property
    def number_and_thoroughfare_or_locality(self):
        """Returns building number and first thoroughfare or locality"""
        return self._concatenate(['building_number', 'first_thoroughfare_or_locality'])

    @property
    def sub_name_and_name(self):
        """Returns sub-building name and building name"""
        return self._concatenate(['sub_building_name', 'building_name'])

    def is_exception_i(self, attr):
        """Returns if first and last characters are numeric"""
        return re.fullmatch(r'^[\d](?:.*[\d])?$', getattr(self, attr, None))

    def is_exception_ii(self, attr):
        """Returns if first and penultimate characters are numeric, and last is alphabetic"""
        return re.fullmatch(r'^([\d][a-zA-Z]|[\d].*?[\d][a-zA-Z])$', getattr(self, attr, None))

    def is_exception_iii(self, attr):
        """Returns if single non-whitespace character"""
        return re.fullmatch(r'^[^ \t\r\n\v\f]$', getattr(self, attr, None))

    def is_exception(self, attr):
        """Returns if value is an exception"""
        return(
            self.is_exception_i(attr) or
                self.is_exception_ii(attr) or
                self.is_exception_iii(attr)
            )

    def _concatenate(self, keys, concatenator=' '):
        """Returns specified attributes concatenated with a specified separator"""
        return concatenator.join(filter(None, [getattr(self, k, None) for k in keys]))
