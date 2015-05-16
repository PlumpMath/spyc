import sys

sys.path.insert(0, '.')

import tempfile
import os

from file_res import File, RegularFile, AbsentFile, Directory
import res

tmpdir = tempfile.mkdtemp()

filename = os.path.join(tmpdir, 'test-hello')

RegularFile(filename,
            source='hello')

File(filename).apply()

with open(filename) as f:
    assert f.read() == 'hello'

res.instances = {}

AbsentFile(filename).apply()

assert not os.path.exists(filename)

res.instances = {}

Directory(filename).apply()

assert os.path.isdir(filename)

os.rmdir(filename)
os.rmdir(tmpdir)
