


class Resource(object):

    def __init__(self, cls):
        self.cls = cls
        self.instances = {}


    def __call__(self, name, *args, **kwargs):
        if name in self.instances:
            obj = self.instances[name]
        else:
            obj = self.cls(name, *args, **kwargs)
            self.instances[name] = obj
        obj.ensure(*args, **kwargs)
        return obj



@Resource
class File(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        print('init: ' + name)

    def ensure(self, *args, **kwargs):
        print('ensure %s(*%r, **%r)' %
              (self.name, args, kwargs))


File('foo')
File('foo')
File('bar')
