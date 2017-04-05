class Node(object):

    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):

    def __init__(self, source, destination):
        """Assumes source and destination are of class Node"""
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def __str__(self):
        return "{} -> {}".format(self.source.get_name(), self.destination.get_name())


class Diagraph(object):
    """Edges is a dictionary mapping each node to a list of its children"""

    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        source = edge.get_source()
        destination = edge.get_destination()
        if not (source in self.edges and destination in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(destination)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for node in self.edges:
            if node.get_name() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for source in self.edges:
            for destination in self.edges[source]:
                result += "{} -> {}\n".format(source.get_name(), destination.get_name())
        return result[:-1]  # omit final newline


class Graph(Diagraph):

    def add_edge(self, edge):
        super().add_edge(edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        super().add_edge(rev)


def build_city_graph(graph_type):
    g = graph_type()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.add_node(Node(name))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g

print(build_city_graph(Diagraph), '\n\n', build_city_graph(Graph), '\n\n')


def print_path(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i is not len(path) - 1:
            result += ' -> '
    return result


def DFS(graph, start, end, path, shortest, to_print=False):
    """Depth First Search.
            Assumes graph is a Diagraph; start and end are nodes;
                    path and shortest are lists of nodes.
            Returns shortest path from start to end in graph"""
    path += [start]
    if to_print:
        print("Current DFS path:", print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, to_print)
            if new_path is not None:
                shortest = new_path
        elif to_print:
            print("Already visited", node)
    return shortest


def shortest_path(graph, start, end, to_print=False):
    """Assumes graph is a Diagraph; start and end are nodes
            Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, to_print)


def test_shortest_path(source, destination):
    g = build_city_graph(Diagraph)
    sp = shortest_path(g, g.get_node(source), g.get_node(destination), to_print=True)
    if sp is not None:
        print("Shortest path from {} to {} is {}.".format(source, destination, print_path(sp)))
    else:
        print("There is no path from {} to {}".format(source, destination))

test_shortest_path('Chicago', 'Boston')
test_shortest_path('Boston', 'Phoenix')


def BFS(graph, start, end, to_print=False):
    """Breadth-first Search.
            Assumes graph is a Diagraph; start and end are nodes.
            Returns a shortest path from start to end in graph"""
    initial_path = [start]
    path_queue = [initial_path]
    while len(path_queue) is not 0:
        # Get and remove oldest element in path_queue
        temporary_path = path_queue.pop(0)
        if to_print:
            print("Current BFS path:", print_path(temporary_path))
        last_node = temporary_path[-1]
        if last_node == end:
            return temporary_path
        for next_node in graph.children_of(last_node):
            if next_node not in temporary_path:
                new_path = temporary_path + [next_node]
                path_queue.append(new_path)
    return None


def shortest_path(graph, start, end, to_print=False):
    """Assumes graph is a Diagraph; start and end are nodes
            Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, to_print)

test_shortest_path('Boston', 'Phoenix')


class WeightedEdge(Edge):

    def __init__(self, source, destination, weight):
        super().__init__(source, destination)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return "{}->{} ({})".format(super().get_source(), super().get_destination(), self.get_weight())
