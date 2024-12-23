import osmnx as ox
import matplotlib.pyplot as plt

# Thu thập dữ liệu
def thu_thap_du_lieu():
    areas = [
        'Ninh Hoa, Khanh Hoa, Vietnam',
        'Tuy Hoa, Phu Yen, Vietnam'
    ]
    
    for i, area in enumerate(areas):
        G = ox.graph_from_place(area, network_type='drive')
        filepath = f'area_{i}.graphml'
        ox.save_graphml(G, filepath=filepath)
        print(f"Đồ thị cho {area} đã được lưu tại {filepath}")

# Kiểm tra và hiển thị dữ liệu
def kiem_tra_du_lieu(filepath):
    G = ox.load_graphml(filepath)
    fig, ax = ox.plot_graph(G, show=False, close=False)
    img_filepath = filepath.replace('.graphml', '.png')
    fig.savefig(img_filepath, dpi=300)
    print(f"Đồ thị đã được hiển thị và lưu tại {img_filepath}")
    plt.show()

if __name__ == "__main__":
    # Gọi hàm thu thập dữ liệu
    thu_thap_du_lieu()
    
    # Kiểm tra và hiển thị đồ thị cho khu vực đầu tiên làm ví dụ
    kiem_tra_du_lieu('area_0.graphml')
