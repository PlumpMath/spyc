"""Support code for writing tests"""

from . import spec


class Failure(Exception):
    pass


class SetElement(spec.Spec):

    def __init__(self, elt, containing_set):
        spec.Spec.__init__(self)
        self.elt = elt
        self.containing_set = containing_set

    def apply(self):
        self.containing_set.add(self.elt)

    def key(self):
        return (SetElement, id(self.containing_set), self.elt)


class Fail(spec.Spec):

    def __init__(self, ident):
        spec.Spec.__init__(self)
        self.ident = ident

    def key(self):
        return (Fail, self.ident)

    def apply(self):
        raise Failure()
