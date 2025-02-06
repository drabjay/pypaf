"""Lineable Mixin"""

from itertools import chain
from .thoroughfare_locality import ThoroughfareLocalityMixin

class LineableMixin(ThoroughfareLocalityMixin):
    """Converts Paf address elements into list of address lines"""

    @classmethod
    @property
    def optional_lines_attrs(cls):
        """Returns optional Paf address line attributes"""
        return cls.organisation_attrs + ['po_box', 'premises', 'thoroughfares_and_localities']

    @classmethod
    @property
    def lines_attrs(cls):
        """Returns optional Paf address line attributes and post_town"""
        return cls.optional_lines_attrs + ['post_town']

    @property
    def optional_lines(self):
        """Returns Paf as list of address lines, excluding post_town and postcode"""
        return self._lines(self.__class__.optional_lines_attrs)

    @property
    def lines(self):
        """Returns Paf as list of address lines, excluding postcode"""
        return self._lines(self.__class__.lines_attrs)

    @property
    def po_box(self):
        """Returns PO Box"""
        return '' if self.is_empty('po_box_number') else f"PO BOX {getattr(self, 'po_box_number')}"

    def _lines(self, attrs):
        """Returns list of address lines from specified attributes"""
        lines = list(filter(None, [getattr(self, k, None) for k in attrs]))
        return list(chain(*[line if isinstance(line, list) else [line] for line in lines]))
