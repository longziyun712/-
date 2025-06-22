def bellman_ford(graph, V, source):
    # 初始化距离
    dist = [float('inf')] * V
    dist[source] = 0
    # 松弛 V-1 次
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # 检测负权环
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("图中存在负权环")
            return None
    return dist
# 图是边列表，每条边是 (起点, 终点, 权重)
edges = [(0, 1, 5), (0, 2, 4),(1, 3, 3),(2, 1, 6), (3, 2, -2)]
V = 4
source = 0
print(bellman_ford(edges, V, source))
