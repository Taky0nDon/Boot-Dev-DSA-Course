class Graph:
    def breadth_first_search(self, v):
        """
        used for:
            - shortest path
            - web crawling
        - good when desired node is close to starting point
        - more memory intensive than DFS
        - return vertices in the order they were visited
        """
        visited = []
        to_visit = [] # TODO: use an actual queue.
        to_visit.append(v)

        while len(to_visit) > 0:
            current_v = to_visit.pop(0)
            visited.append(current_v)
            neighbors = sorted(self.graph[current_v])
            for vertex in neighbors:
                if not (vertex in visited or vertex in to_visit):
                    to_visit.append(vertex)
        return visited

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

