import osmnx as ox
import networkx as nx
import time

class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return None
        return dist

def main():
    G = ox.load_graphml('area_0.graphml')
    nodes = list(G.nodes)
    g = BellmanFord(len(nodes))

    for u, v, data in G.edges(data=True):
        weight = data.get('length', 1)
        g.add_edge(nodes.index(u), nodes.index(v), weight)
        g.add_edge(nodes.index(v), nodes.index(u), weight)

    source_node = 0
    start_time = time.time()
    bellman_ford_distances = g.bellman_ford(source_node)
    end_time = time.time()
    bf_time = end_time - start_time
    
    if bellman_ford_distances is not None:
        print("Khoảng cách từ Bellman-Ford:", bellman_ford_distances)
        print("Thời gian thực hiện Bellman-Ford:", bf_time, "seconds")

if __name__ == "__main__":
    main()
