class Graph:
    def __init__(self, num_vertices):
        self.graph = [[False]*num_vertices for _ in range(num_vertices)]
        # no fancy list comprehension
        # self.graph = []
        # for vertex in range(num_vertices):
        #     connections = []
        #     for vertex in range(num_vertices):
        #         connections.append(False)
        #     self.graph.append(connections)

    def add_edge(self, u, v):
        if not (len(self.graph) > u >= 0 and len(self.graph) > v >= 0):
            raise ValueError("Impossible node")
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

