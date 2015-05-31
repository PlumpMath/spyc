from spyc.spec import Spec

import os


class File(Spec):

    def __init__(self, path, **kwargs):
        Spec.__init__(self)
        self.path = path
        Spec.ensure(self, **kwargs)

    def key(self):
        return (File, self.path)


class AbsentFile(File):

    def apply(self):
        if os.path.exists(self.path):
            os.remove(self.path)


class RegularFile(File):

    def apply(self):
        if os.path.exists(self.path) and not os.path.isfile(self.path):
            os.remove(self.path)
        with open(self.path, 'wb') as f:
            f.write(self['source'])
        if self['mode'] is not None:
            os.chmod(self.path, self['mode'])


class Directory(File):

    def apply(self):
        if os.path.exists(self.path) and not os.path.isdir(self.path):
            os.remove(self.path)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if self['mode'] is not None:
            os.chmod(self.path, self['mode'])
