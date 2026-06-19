"""Thoroughfare and Locality Mixin"""


class ThoroughfareLocalityMixin():
    """Thoroughfare and locality processing"""

    dependent_thoroughfare_attrs = (
        'dependent_thoroughfare_name', 'dependent_thoroughfare_descriptor'
        )
    thoroughfare_attrs = ('thoroughfare_name', 'thoroughfare_descriptor')
    locality_attrs = ('double_dependent_locality', 'dependent_locality')
    thoroughfare_and_locality_attrs = (
        ('dependent_thoroughfare', 'thoroughfare') + locality_attrs
        )

    @property
    def thoroughfares_and_localities(self):
        """Returns thoroughfares and localities list"""
        attrs = self.thoroughfare_and_locality_attrs
        return [getattr(self, k) for k in attrs if not self.is_used_or_empty(k)]

    @property
    def dependent_thoroughfare(self):
        """Returns dependent thoroughfare"""
        return ' '.join(
            filter(None, [getattr(self, k, None) for k in self.dependent_thoroughfare_attrs]))

    @property
    def thoroughfare(self):
        """Returns thoroughfare"""
        return ' '.join(filter(None, [getattr(self, k, None) for k in self.thoroughfare_attrs]))

    @property
    def first_thoroughfare_or_locality_attr(self):
        """Returns name of first populated thoroughfare / locality attribute"""
        for k in self.thoroughfare_and_locality_attrs:
            if not self.is_empty(k):
                return k
        return None

    @property
    def first_thoroughfare_or_locality(self):
        """Returns first populated thoroughfare or locality value"""
        attr = self.first_thoroughfare_or_locality_attr
        return getattr(self, attr) if attr is not None else ''

    def is_used_or_empty(self, attr):
        """Returns if attribute value is empty or has already been used"""
        if self.is_empty(attr):
            return True
        return (
            attr == self.first_thoroughfare_or_locality_attr
            and self.premises.includes_first_thoroughfare_or_locality
            )
