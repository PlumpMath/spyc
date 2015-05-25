
instances = {}


class Conflict(Exception):

    def __init__(self, resource, key, existing, new):
        self.resource = resource
        self.key = key
        self.existing = existing
        self.new = new


class Resource(object):

    def __init__(self, name, *args, **kwargs):
        if hasattr(self, 'name'):
            # We've already been initialized once, stop here.
            self.needs_init = False
            return
        self.needs_init = True
        self.name = name
        self.options = {}
        if hasattr(self, 'name_attr'):
            self.options[self.name_attr] = self.name
        self.ensure(*args, **kwargs)

    def ensure(self, *args, **kwargs):
        for key in kwargs.keys():
            if key not in self.options:
                self.options[key] = kwargs[key]
            elif self.options[key] != kwargs[key]:
                raise Conflict(self, key, self.options[key], kwargs[key])

    def __getitem__(self, key):
        if key in self.options:
            return self.options[key]
        else:
            return getattr(self, key)

    def __new__(cls, name, *args, **kwargs):
        if (cls, name) in instances:
            return instances[(cls, name)]
        else:
            obj = object.__new__(cls, name, *args, **kwargs)
            Resource.add_instance(cls, name, obj)
            instances[(cls, name)] = obj
            return obj

    @staticmethod
    def add_instance(cls, name, obj):
        instances[(cls, name)] = obj
        for superclass in cls.__bases__:
            if Resource.__subclasscheck__(superclass):
                Resource.add_instance(superclass, name, obj)


class File(Resource):
    pass
