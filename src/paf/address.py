"""PAF Address"""

# Tried using dataclasses.dataclass(frozen=True) decorator for immutablity but did not work"""
from .immutable import ImmutableMixin
from .lineable import LineableMixin

class Address(ImmutableMixin, LineableMixin):
    """Main PAF Address class"""

    def __init__(self, args):
        """Initialise Address elements"""
        for key in self.__class__.attrs: # pylint: disable=not-an-iterable
            object.__setattr__(self, key, '')
        for key, val in args.items():
            if hasattr(self, key):
                object.__setattr__(self, key, val)
        self.extend_premises()

    def __repr__(self):
        """Return full representation of an Address"""
        args = {k: getattr(self, k) for k in self.__class__.attrs if getattr(self, k, None)} # pylint: disable=not-an-iterable
        return self.__class__.__name__ + '(' + str(args) + ')'

    def __str__(self):
        """Return Address as string representation"""
        line = ', '.join(self.lines)
        if self.is_empty('postcode'):
            return line
        return '. '.join([line] + [getattr(self, 'postcode')])

    def __iter__(self):
        """Return Address as iterable"""
        yield from self.lines.__iter__()
        if not self.is_empty('postcode'):
            yield from [getattr(self, 'postcode')].__iter__()

    def as_str(self):
        """Return Address as string"""
        return str(self)

    def as_list(self):
        """Return Address as list of strings"""
        return list(self)

    def as_tuple(self):
        """Return Address as tuple of strings"""
        return tuple(self)
