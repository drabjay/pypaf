"""Attribute Mixin"""


class AttributeMixin():
    """Address elements and derived properties"""

    premises_attrs = (
        'organisation_name', 'department_name',
        'sub_building_name', 'building_name', 'building_number',
        'po_box_number'
        )
    post_attrs = ('post_town', 'postcode')
    other_attrs = ('concatenation_indicator', 'udprn')

    @property
    def attrs(self):
        """Returns all Paf address elements"""
        return (
            self.premises_attrs
            + self.dependent_thoroughfare_attrs
            + self.thoroughfare_attrs
            + self.locality_attrs
            + self.post_attrs
            + self.other_attrs
            )

    def is_empty(self, attr):
        """Returns if attribute value is empty"""
        return getattr(self, attr, '') == ''
