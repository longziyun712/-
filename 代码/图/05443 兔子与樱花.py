n = int(input())
locations = [input().strip() for _ in range(n)]
distances = [[float('inf')] * n for _ in range(n)]
next_node = [[-1] * n for _ in range(n)]
for i in range(n):
    distances[i][i] = 0
for _ in range(int(input())):
    a, b, d = input().split()
    u, v, dist = locations.index(a), locations.index(b), int(d)
    if dist < distances[u][v]:
        distances[u][v] = distances[v][u] = dist
        next_node[u][v] = v
        next_node[v][u] = u
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                next_node[i][j] = next_node[i][k]
def reconstruct_path(next_node,u, v, locations, distances):
    path_indices = [u]
    while u != v:
        u = next_node[u][v]
        path_indices.append(u)
        # 构造格式化路径字符串
    result = locations[path_indices[0]]
    for i in range(1, len(path_indices)):
        from_idx, to_idx = path_indices[i - 1], path_indices[i]
        result += f"->({distances[from_idx][to_idx]})->{locations[to_idx]}"
    return result
for _ in range(int(input())):
            a, b = input().split()
            u, v = locations.index(a), locations.index(b)
            if distances[u][v] ==float('inf') :
                print("No path")
            else:
                print(reconstruct_path(next_node, u, v, locations, distances))
