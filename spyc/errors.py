
class MergeConflict(Exception):
    """Two conflicting specs could not be merged."""

    def __init__(self, key, constraint, old, new):
        self.key = key
        self.constraint = constraint
        self.old = old
        self.new = new
