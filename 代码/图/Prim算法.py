import heapq
def prim(graph, start):
    """ :param graph: 邻接表表示的图，格式 {u: [(v, weight), ...]}
    :param start: 起始顶点
    :return: MST 的边列表 [(u, v, weight), ...]"""
    V = len(graph)
    visited = [False] * V  # 记录顶点是否已加入 MST
    heap = []  # 优先队列（最小堆）
    mst_edges = []  # 存储 MST 的边
    # 初始化：将起始点的所有边加入堆
    visited[start] = True
    for v, weight in graph[start]:
        heapq.heappush(heap, (weight, start, v))
    while heap and len(mst_edges) < V - 1:
        weight, u, v = heapq.heappop(heap)
        if visited[v]:
            continue  # 跳过已访问的顶点
        visited[v] = True
        mst_edges.append((u, v, weight))
        # 将新加入顶点的边加入堆
        for neighbor, w in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(heap, (w, v, neighbor))
    return mst_edges