from spyc.graph import Vertex


class Scheduler(object):

    def __init__(self):
        self.specs = {}

    def ensure(self, spec):
        """Require that ``spec`` is satisfied."""
        if spec.key() in self.specs:
            self.specs[spec.key()].data.merge(spec)
        else:
            self.specs[spec.key()] = Vertex(spec)

    def depend(self, first, next):
        """Specify that ``first`` depends on ``next``.

        This also has the effect of invoking ``ensure`` on both resources.
        """
        first.schedule(self)
        next.schedule(self)
        self.specs[first.key()].edges.add(self.specs[next.key()])
