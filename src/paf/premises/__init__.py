"""Address Premises"""

from ..initiator import attribute_init
from ..immutable import ImmutableMixin
from ..thoroughfare_locality import ThoroughfareLocalityMixin
from .attribute import AttributeMixin
from .lineable import LineableMixin
from .split import SplitMixin
from .rule000 import Rule000
from .rule001 import Rule001
from .rule010 import Rule010
from .rule011 import Rule011
from .rule100 import Rule100
from .rule101 import Rule101
from .rule110 import Rule110
from .rule111 import Rule111


class Premises(
        ImmutableMixin, AttributeMixin,
        ThoroughfareLocalityMixin, LineableMixin, SplitMixin
        ):
    """PAF Address Premises class"""

    def __new__(cls, *args, **kwargs):
        """Create subclass instance based on the presence of building attributes"""
        if cls is Premises:
            elements = kwargs if kwargs else (args[0] if args else {})
            rule_num = ''.join(['0' if not elements.get(k) else '1' for k in cls.building_attrs])
            subclass_name = f'PremisesRule{rule_num}'
            return object.__new__(globals().get(subclass_name))
        return object.__new__(cls)

    @attribute_init
    def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Initialise Premises elements"""

    def __repr__(self):
        """Return full representation of a Premises"""
        args = {k: getattr(self, k) for k in list(self.attrs) if getattr(self, k, None)}
        return 'Premises(' + str(args) + ')'

    def __str__(self):
        """Return Premises as string representation"""
        return ', '.join(self.lines)

    def __iter__(self):
        """Return Premises as iterable"""
        yield from list(self.lines)

    def __call__(self):
        """Return Premises as dictionary"""
        return self.as_premisable()  # pylint: disable=no-member

    @property
    def building_number_and_sub_building_name(self):
        """Returns building number and sub-building name"""
        return self._concatenate(('building_number', 'sub_building_name'), '')

    @property
    def name_and_thoroughfare_or_locality(self):
        """Returns building number and first thoroughfare or locality"""
        return self._concatenate(('building_name', 'first_thoroughfare_or_locality'))

    @property
    def name_last_word_and_thoroughfare_or_locality(self):
        """Returns last word of building name and first thoroughfare"""
        return self._concatenate(('building_name_last_word', 'first_thoroughfare_or_locality'))

    @property
    def number_and_thoroughfare_or_locality(self):
        """Returns building number and first thoroughfare or locality"""
        return self._concatenate(('building_number', 'first_thoroughfare_or_locality'))

    @property
    def number_sub_name_and_thoroughfare_or_locality(self):
        """Returns building number, sub-building name and first thoroughfare"""
        return self._concatenate(
            ('building_number_and_sub_building_name', 'first_thoroughfare_or_locality')
            )

    @property
    def sub_name_and_name(self):
        """Returns sub-building name and building name"""
        return self._concatenate(('sub_building_name', 'building_name'))

    @property
    def sub_name_comma_name(self):
        """Returns sub-building name and building name joined with a comma"""
        return self._concatenate(('sub_building_name', 'building_name'), ', ')

    @property
    def sub_name_and_thoroughfare_or_locality(self):
        """Returns sub-building number and first thoroughfare or locality"""
        return self._concatenate(('sub_building_name', 'first_thoroughfare_or_locality'))

    @property
    def sub_and_building_name_but_last_word(self):
        """Returns sub-building name and but last word of the building name"""
        return self._concatenate(('sub_building_name', 'building_name_but_last_word'))

    @property
    def building_name_but_last_word(self):
        """Returns all but last word of the building name"""
        return self.but_last_word('building_name')

    @property
    def building_name_last_word(self):
        """Returns last word of the building name"""
        return self.last_word('building_name')

    @property
    def building_name_last_two_words(self):
        """Returns last two words of the building name"""
        return self.last_two_words('building_name')

    @property
    def sub_building_name_but_last_word(self):
        """Returns all but last word of the sub-building name"""
        return self.but_last_word('sub_building_name')

    @property
    def sub_building_name_last_word(self):
        """Returns last word of the sub-building name"""
        return self.last_word('sub_building_name')

    def _concatenate(self, keys, concatenator=' '):
        """Returns specified attributes concatenated with a separator"""
        return concatenator.join(
            filter(None, [getattr(self, k, None) for k in keys])
            )

# pylint: disable=too-many-ancestors

class PremisesRule000(Premises, Rule000):
    """Rule 000 Premises subclass"""


class PremisesRule001(Premises, Rule001):
    """Rule 001 Premises subclass"""


class PremisesRule010(Premises, Rule010):
    """Rule 010 Premises subclass"""


class PremisesRule011(Premises, Rule011):
    """Rule 011 Premises subclass"""


class PremisesRule100(Premises, Rule100):
    """Rule 100 Premises subclass"""


class PremisesRule101(Premises, Rule101):
    """Rule 101 Premises subclass"""


class PremisesRule110(Premises, Rule110):
    """Rule 110 Premises subclass"""


class PremisesRule111(Premises, Rule111):
    """Rule 111 Premises subclass"""

# pylint: enable=too-many-ancestors
