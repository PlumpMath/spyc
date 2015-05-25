from abc import ABCMeta, abstractmethod
from spyc.errors import MergeConflict


class Spec(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.__constraints = {}

    def __setitem__(self, key, value):
        self.__constraints[key] = value

    def __getitem__(self, key):
        return self.__constraints[key]

    def schedule(self, scheduler):
        scheduler.ensure(self)

    @abstractmethod
    def key(self):
        """Return a unique (hashable) identifier identifying the resource."""

    def merge(self, other):
        """Merge the the constraints in ``other`` into ``self``.

        raise ``MergeConflict`` on error.
        """
        for key in other.__constraints.keys():
            if key in self.__constraints:
                if self[key] != other[key]:
                    raise MergeConflict(self.key(), key, self[key], other[key])
            else:
                self[key] = other[key]

    def ensure(self, **kwargs):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        return self
