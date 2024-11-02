class Vertex:

    def __init__(self, key) -> None:
        self.key = key
        self.connections = {}

    
    def add_adj(self, vertex, weight=0):
        self.connections[vertex] = weight

    
    def get_connections(self):
        return self.connections.keys()
    

    def get_weight(self, vertex):
        return self.connections[vertex]
    

class Graph:
        
    def __init__(self) -> None:
        self.vertex_dict = {}

    
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex
    

    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None
    

    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 10)
    vertex_a = graph.get_vertex("A")
    vertex_b = graph.get_vertex("B")