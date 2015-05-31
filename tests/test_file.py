import tempfile
import os

from spyc.file import File, RegularFile, AbsentFile, Directory

tmpdir = tempfile.mkdtemp()
filename = os.path.join(tmpdir, 'test-hello')

f_spec = RegularFile(filename)
f_spec['source'] = 'hello'
f_spec.apply()
with open(filename) as f:
    assert f.read() == 'hello'

AbsentFile(filename).apply()
assert not os.path.exists(filename)

Directory(filename).apply()
assert os.path.isdir(filename)

os.rmdir(filename)
os.rmdir(tmpdir)
