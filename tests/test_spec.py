from spyc.spec import Spec
from spyc.errors import MergeConflict
import pytest


class Foo(Spec):

    def __init__(self, ident):
        Spec.__init__(self)
        self.ident = ident

    def key(self):
        return (Foo, self.ident)

assert Foo('one').ensure(a='b')['a'] == 'b'


with pytest.raises(MergeConflict):
    Foo('one').ensure(a='b').merge(Foo('one').ensure(a='c'))

foo = Foo('one').ensure(a='b')
foo.merge(Foo('one').ensure(b='c'))
assert foo['a'] == 'b'
assert foo['b'] == 'c'

# This should *not* raise exception:
Foo('one').ensure(a='b').merge(Foo('one').ensure(a='b'))
