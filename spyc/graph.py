
class Vertex(object):

    def __init__(self, data):
        self.edges = set()
        self.data = data


def find_cycle(graph):
    """Attempt to find a cycle in ``graph``.

    ``graph`` may either be a ``Vertex`` or a ``set`` of verticies,
    and will be used as the starting point of the search. ``find_cycle``
    will return the first cycle reachable from ``graph``, or ``None``
    if no cycle can be found. The cycle will be represented as a list
    off the verticies it contains, in order. The last element in the list
    will have an edge to the first.
    """
    # We're absuing exceptions here more than a little. When/if a cycle
    # is found, we raise an exception containing the result, and catch
    # it here. If the cycle is never thrown, return None.
    if isinstance(graph, Vertex):
        graph = set([graph])
    try:
        _find_cycle(graph, [], set(), set())
    except _FoundCycle as e:
        return e.path
    return None


def _find_cycle(graph, path, path_set, visited):
    """Helper function, doing most of the work for ``find_cycle``.

    * ``graph`` is the same as in ``find_cycle``.
    * ``path`` is an (ordered) list of the nodes that are part of the current
      path from the root.
    * ``path_set`` is a set containing the same elements as ``path``; this
      is used for faster membership checking, while ``path`` is thrown as
      the "found" cycle.
    """
    # Depth first search tracking visited verticies and our current path.
    # If we find a node we've visited *in this path*, throw the path back
    # to the top.
    for vertex in graph:
        if vertex in path_set:
            raise _FoundCycle(path)
        if vertex in visited:
            continue
        path.append(vertex)
        path_set.add(vertex)
        visited.add(vertex)
        _find_cycle(vertex.edges, path, path_set, visited)
        path.pop()
        path_set.remove(vertex)


class _FoundCycle(Exception):

    def __init__(self, path):
        self.path = path
