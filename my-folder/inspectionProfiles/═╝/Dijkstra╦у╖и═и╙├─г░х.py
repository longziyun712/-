import heapq
def dijkstra(graph, start):
    # 初始化距离数组
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    # 优先队列：(距离, 节点)
    heap = [(0, start)]
    while heap:
        current_dist, node = heapq.heappop(heap)
        # 如果当前距离大于已知最短距离，跳过
        if current_dist > dist[node]:
            continue
        # 遍历所有邻居
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            # 如果找到更短路径
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist


#记录路径
# 添加prev数组记录前驱节点
def dijkstra_with_path(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n  # 记录前驱节点
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u  # 记录前驱节点
                heapq.heappush(heap, (new_dist, v))
    return dist, prev
# 重建路径
def get_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    return path[::-1]  # 反转得到正向路径