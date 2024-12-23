import osmnx as ox
import matplotlib.pyplot as plt

def hien_thi_ket_qua(G, path, title):
    fig, ax = ox.plot_graph(G, node_color='blue', edge_color='gray', node_size=20, edge_linewidth=1, show=False, close=False)
    # Highlight the path
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        ox.plot_graph_route(G, route=[u, v], route_color='red', route_linewidth=2, ax=ax, show=False)
    plt.title(title)
    plt.show()

def hien_thi_diem_quan_trong(G, important_nodes, title):
    fig, ax = ox.plot_graph(G, node_color='blue', edge_color='gray', node_size=20, edge_linewidth=1, show=False, close=False)
    # Highlight the important nodes
    for node in important_nodes:
        x, y = G.nodes[node]['x'], G.nodes[node]['y']
        ax.plot(x, y, 'ro', markersize=10)
    plt.title(title)
    plt.show()

def tao_bieu_do():
    # Dữ liệu giả sử về thời gian thực hiện (ms) và độ chính xác (%)
    giai_thuat = ['Bellman-Ford', 'Dijkstra']
    thoi_gian = [150, 50]
    do_chinh_xac = [98, 99]

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Giải thuật')
    ax1.set_ylabel('Thời gian (ms)', color=color)
    ax1.bar(giai_thuat, thoi_gian, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Độ chính xác (%)', color=color)
    ax2.plot(giai_thuat, do_chinh_xac, color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title("So sánh thời gian và độ chính xác của giải thuật")
    plt.show()

def tao_bieu_do_so_sanh(thoi_gian_bf, thoi_gian_dijkstra, do_chinh_xac):
    giai_thuat = ['Bellman-Ford', 'Dijkstra']
    thoi_gian = [thoi_gian_bf, thoi_gian_dijkstra]

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Giải thuật')
    ax1.set_ylabel('Thời gian (s)', color=color)
    ax1.bar(giai_thuat, thoi_gian, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Độ chính xác (%)', color=color)
    ax2.plot(giai_thuat, do_chinh_xac, color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title("So sánh thời gian và độ chính xác của giải thuật")
    plt.show()

# Để kiểm tra chức năng của hàm
if __name__ == "__main__":
    thoi_gian_bf = 2.0  # Thời gian thực hiện Bellman-Ford (giả sử 2 giây)
    thoi_gian_dijkstra = 0.5  # Thời gian thực hiện Dijkstra (giả sử 0.5 giây)
    do_chinh_xac = [98, 99]  # Độ chính xác giả sử
    tao_bieu_do_so_sanh(thoi_gian_bf, thoi_gian_dijkstra, do_chinh_xac)
