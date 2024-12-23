import subprocess
import os
import osmnx as ox
import hien_thi_ket_qua as ht
import time
import heapq  # Thêm import heapq

# Đảm bảo chạy từ thư mục chứa các tệp mã
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# Hàm chạy giải thuật và trả về thời gian thực hiện
def chay_giai_thuat(ten_file):
    result = subprocess.run(["python", ten_file], capture_output=True, text=True)
    thoi_gian = None
    for line in result.stdout.split("\n"):
        if "seconds" in line:
            thoi_gian = float(line.split()[-2])
    return thoi_gian

# Hàm khai báo và định nghĩa BellmanFord và Dijkstra
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

# Hàm so sánh kết quả của hai giải thuật
def so_sanh_ket_qua(graph, nodes):
    # Thực hiện giải thuật Bellman-Ford
    bf = BellmanFord(len(nodes))
    for u in graph:
        for v, w in graph[u]:
            bf.add_edge(u, v, w)
    
    source_node = 0
    
    start_time = time.time()
    bellman_ford_distances = bf.bellman_ford(source_node)
    bf_time = time.time() - start_time
    
    if bellman_ford_distances is not None:
        print("Khoảng cách từ Bellman-Ford:", bellman_ford_distances)
        print("Thời gian thực hiện Bellman-Ford:", bf_time, "seconds")
    
    # Thực hiện giải thuật Dijkstra
    start_time = time.time()
    dijkstra_distances = dijkstra(graph, source_node)
    dijkstra_time = time.time() - start_time
    
    print("Khoảng cách từ Dijkstra:", dijkstra_distances)
    print("Thời gian thực hiện Dijkstra:", dijkstra_time, "seconds")

    # So sánh khoảng cách
    for i in range(len(bellman_ford_distances)):
        if bellman_ford_distances[i] != dijkstra_distances[i]:
            print(f"Sự khác biệt tại nút {i}: Bellman-Ford = {bellman_ford_distances[i]}, Dijkstra = {dijkstra_distances[i]}")

def main():
    # Bước 1 và 2: Thu Thập và Kiểm Tra Dữ Liệu
    subprocess.run(["python", "thu_thap_va_kiem_tra_du_lieu.py"])

    # Bước 3: Sử dụng giải thuật Bellman-Ford
    bf_time = chay_giai_thuat("bellman_ford_osmnx.py")
    
    # Bước 4: Sử dụng giải thuật Dijkstra
    dijkstra_time = chay_giai_thuat("dijkstra_osmnx.py")
    
    # Tải đồ thị từ file
    G = ox.load_graphml('area_0.graphml')
    nodes = list(G.nodes)
    graph = {i: [] for i in range(len(nodes))}
    
    for u, v, data in G.edges(data=True):
        weight = data.get('length', 1)
        graph[nodes.index(u)].append((nodes.index(v), weight))
        graph[nodes.index(v)].append((nodes.index(u), weight))

    # So sánh kết quả
    so_sanh_ket_qua(graph, nodes)
    
    # Hiển thị kết quả
    dijkstra_path = [0, 1, 2, 3, 4]  # Đây là ví dụ đường đi từ Dijkstra
    bellman_ford_path = [0, 1, 3, 4]  # Đây là ví dụ đường đi từ Bellman-Ford

    # Hiển thị kết quả
    ht.hien_thi_ket_qua(G, dijkstra_path, "Đường đi ngắn nhất từ Dijkstra")
    ht.hien_thi_ket_qua(G, bellman_ford_path, "Đường đi ngắn nhất từ Bellman-Ford")

    # Hiển thị các điểm quan trọng
    important_nodes = [0, 1, 2, 3, 4]  # Giả sử các điểm quan trọng là các node có chỉ số từ 0 đến 4
    ht.hien_thi_diem_quan_trong(G, important_nodes, "Các điểm quan trọng tại Tuy Hòa")

    # Tạo biểu đồ so sánh
    do_chinh_xac = [98, 99]  # Giả sử độ chính xác tương tự
    ht.tao_bieu_do_so_sanh(bf_time, dijkstra_time, do_chinh_xac)

if __name__ == "__main__":
    main()
