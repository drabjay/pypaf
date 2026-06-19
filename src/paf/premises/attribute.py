"""Attribute Mixin"""


class AttributeMixin():
    """Premises elements and derived properties"""

    organisation_attrs = ('organisation_name', 'department_name')
    building_attrs = ('sub_building_name', 'building_name', 'building_number')
    other_attrs = ('po_box_number', 'concatenation_indicator')

    @property
    def attrs(self):
        """Returns all Paf premises elements"""
        return (
            self.organisation_attrs
            + self.building_attrs
            + self.dependent_thoroughfare_attrs
            + self.thoroughfare_attrs
            + self.locality_attrs
            + self.other_attrs
            )

    def is_empty(self, attr):
        """Returns if attribute value is empty"""
        return getattr(self, attr, '') == ''
