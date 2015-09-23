import tempfile
import os

from spyc.file import RegularFile, AbsentFile, Directory

tmpdir = tempfile.mkdtemp()
filename = os.path.join(tmpdir, 'test-hello')

RegularFile(filename,
            source='hello').apply()
with open(filename) as f:
    assert f.read() == 'hello'

AbsentFile(filename).apply()
assert not os.path.exists(filename)

Directory(filename).apply()
assert os.path.isdir(filename)

os.rmdir(filename)
os.rmdir(tmpdir)
