from spyc.graph import Vertex, find_cycle


elts = range(5)

for i in range(len(elts)):
    elts[i] = Vertex(elts[i])

for i in range(len(elts) - 1):
    elts[i].edges.add(elts[i+1])

assert find_cycle(set(elts)) is None
assert find_cycle(elts[0]) is None
assert find_cycle(elts[0].edges) is None

elts[-1].edges.add(elts[0])

assert len(find_cycle(set(elts))) == len(elts)
assert len(find_cycle(elts[0])) == len(elts)
assert len(find_cycle(elts[0].edges)) == len(elts)
