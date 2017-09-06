from networkx.classes.graph import Graph

class SnapshotGraph(object):
    def __init__(self, **attr):
        self.graphs = {}
        self.graph.update(attr)
        self.snapshots = []

    def add_snapshot(self, edges):
        g = Graph()
        g.add_weighted_edges_from(edges)
        self.snapshots.append(g)

    def degree(self):
        return [g.degree() for g in self.snapshots]

    def number_of_nodes(self):
        return [g.number_of_nodes() for g in self.snapshots]

    def order(self):
        return [g.order() for g in self.snapshots]

    def has_node(self, n):
        return [g.has_node() for g in self.snapshots]

    def degree(self, nbunch=None, weight=None):
        return [g.degree() for g in self.snapshots]

    def is_multigraph(self):
        return [g.is_multigraph() for g in self.snapshots]

    def is_directed(self):
        return [g.is_directed() for g in self.snapshots]

    def to_directed(self):
        return [g.to_directed() for g in self.snapshots]

    def to_undirected(self):
        return [g.to_undirected() for g in self.snapshots]

    def size(self, weight=None):
        return [g.size() for g in self.snapshots]
