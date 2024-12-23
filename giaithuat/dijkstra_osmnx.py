import osmnx as ox
import heapq
import time

def dijkstra(graph, src):
    V = len(graph)
    dist = [float("Inf")] * V
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        (d, u) = heapq.heappop(pq)
        for neighbor, weight in graph[u]:
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

def main():
    G = ox.load_graphml('area_0.graphml')
    nodes = list(G.nodes)
    graph = {i: [] for i in range(len(nodes))}
    
    for u, v, data in G.edges(data=True):
        weight = data.get('length', 1)
        graph[nodes.index(u)].append((nodes.index(v), weight))
        graph[nodes.index(v)].append((nodes.index(u), weight))

    source_node = 0
    start_time = time.time()
    dijkstra_distances = dijkstra(graph, source_node)
    end_time = time.time()
    dijkstra_time = end_time - start_time
    
    print("Khoảng cách từ Dijkstra:", dijkstra_distances)
    print("Thời gian thực hiện Dijkstra:", dijkstra_time, "seconds")

if __name__ == "__main__":
    main()
