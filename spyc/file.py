from spyc.spec import Spec
from spyc.merge import merge_attrs


class File(Spec):

    def __init__(self, path, **kwargs):
        self.path = path
        self['present'] = True
        Spec.ensure(self, **kwargs)

    def key(self):
        return (File, self.path)

    def apply(self):
        if not self['present']:
            pass  # Remove the file
        else:
            # We don't know what kind of file this is?


class RegularFile(File):
    pass


class Directory(File):
    pass
