from collections import deque


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for _ in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m

    # 方向数组：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 初始化距离矩阵和访问矩阵
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    dist[0][0] = 0
    q = deque()
    q.append((0, 0))

    # BFS
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    # 回溯路径
    path = []
    x, y = n - 1, m - 1
    path.append((x + 1, y + 1))  # 题目中的坐标从1开始

    while x != 0 or y != 0:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == dist[x][y] - 1:
                x, y = nx, ny
                path.append((x + 1, y + 1))
                break

    # 输出路径（从起点到终点）
    for coord in reversed(path):
        print(coord[0], coord[1])


if __name__ == "__main__":
    main()