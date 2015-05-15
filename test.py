import os
from os import path

def verify(cond):
    if not cond:
        raise Exception("verify failed!")


class Conflict(Exception):
    pass


class singleton(object):

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

    def __getattr__(self, key):
        getattr(self.cls, key)


class Resource(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.options = {}
        self.ensure(*args, **kwargs)
        if hasattr(self, 'name_attr') and self.name_attr not in self.options:
            self.options[self.name_attr] = self.name

    def __getitem__(self, key):
        if key in self.options:
            return self.options[key]
        else:
            return getattr(self, key)

    def ensure(self, **kwargs):
        for key in kwargs.keys():
            if key in self.options and self.options[key] != kwargs[key]:
                raise Conflict("option set twice to different values")
            else:
                self.options[key] = kwargs[key]


class File(Resource):

    name_attr = 'path'

    state = 'file'
    mode = None

    def check(self):
        verify(self['state'] in ('absent',
                                 'file',
                                 'directory',
                                 ))

    def apply(self):
        predicate = {
            'file': path.isfile,
            'directory': path.isdir,
            'absent': lambda p: not path.exists(p),
        }[self['state']]

        if predicate(self['path']):
            return
        if path.exists(self['state']):
            os.remove(self['path'])

        if self['state'] == 'file':
            self.__write()
        elif self['state'] == 'directory':
            os.mkdir(self['path'])

        if self['mode'] is not None:
            os.chmod(self['path'], self['mode'])

    def __write(self):
        with open(self['path'], 'wb') as f:
            f.write(self['source'])


class AbsentFile(File):

    def apply(self):
        if path.exists(self['path']):
            os.remove(self['path'])


class Directory(File):

    def apply(self):
        if path.exists(self['path']) and not path.isdir(self['path']):
            os.remove(self['path'])
            os.mkdir(self['path'])
        if self['mode'] is not None:
            os.chmod(self['path'], self['mode'])


class RegularFile(File):

    def apply(self):
        if path.exists(self['path']) and not path.isfile(self['path']):
            os.remove(self['path'])
        with open(self['path'], 'wb') as f:
            f.write(self['source'])
        if self['mode'] is not None:
            os.chmod(self['path'], self['mode'])


File('/tmp/foo/test-file',
     source='Hello, world!',
     mode=0400,
     ).apply()
