from spyc.graph import Vertex, find_cycle, topological_sort


elts = map(Vertex, range(5))

for i in range(len(elts) - 1):
    elts[i].edges.add(elts[i+1])

assert find_cycle(set(elts)) is None
assert find_cycle(elts[0]) is None
assert find_cycle(elts[0].edges) is None

elts[-1].edges.add(elts[0])

assert len(find_cycle(set(elts))) == len(elts)
assert len(find_cycle(elts[0])) == len(elts)
assert len(find_cycle(elts[0].edges)) == len(elts)

elts = map(Vertex, range(5))

elts[4].edges.add(elts[0])
elts[4].edges.add(elts[3])
elts[3].edges.add(elts[0])
elts[2].edges.add(elts[1])

sort_result = [v.data for v in topological_sort(elts)]

assert sort_result.index(elts[0].data) < \
    sort_result.index(elts[3].data) < \
    sort_result.index(elts[4].data)
assert sort_result.index(elts[1].data) < sort_result.index(elts[2].data)
