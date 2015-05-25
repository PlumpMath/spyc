import sys
sys.path.insert(0, '.')

from spyc import res

for _ in range(2):
    res.File('/tmp/hello-world')
    assert set(res.instances.keys()) == set([
        (res.Resource, '/tmp/hello-world'),
        (res.File,     '/tmp/hello-world'),
    ])

a = res.File('/tmp/hello-world')
b = res.File('/tmp/hello-world')
assert a is b


res.instances = {}


class Foo(res.Resource):
    pass


class Bar(Foo):
    pass


Foo('cat')
Bar('dog')

assert Foo('dog') is Bar('dog')

assert type(Foo('cat')) is Foo
assert type(Foo('dog')) is Bar

assert set(res.instances.keys()) == set([
    (res.Resource, 'cat'),
    (Foo,          'cat'),
    (res.Resource, 'dog'),
    (Foo,          'dog'),
    (Bar,          'dog'),
])
