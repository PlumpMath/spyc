import os
from os import path
import res


def verify(cond):
    if not cond:
        raise Exception("verify failed!")


class File(res.Resource):
    name_attr = 'path'
    mode = None


class AbsentFile(File):

    def apply(self):
        if path.exists(self['path']):
            os.remove(self['path'])


class Directory(File):

    def apply(self):
        if path.exists(self['path']) and not path.isdir(self['path']):
            os.remove(self['path'])
        if not path.exists(self['path']):
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
