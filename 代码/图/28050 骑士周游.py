def knight_tour():
    import sys
    sys.setrecursionlimit(1000000)  # 防止递归深度过大报错
    n = int(sys.stdin.readline())  # 棋盘大小
    sr, sc = map(int, sys.stdin.readline().split())  # 起始位置
    board = [[-1 for _ in range(n)] for _ in range(n)]  # 初始化棋盘（-1表示未访问）
    # 骑士的8种移动方向（“日”字形）
    moves = [ (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)]
    def is_valid(x, y):
        """检查位置(x,y)是否在棋盘内且未访问"""
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    def get_next_moves(x, y):
        """动态排序下一步：优先选择后续分支少的位置（Warnsdorff规则）"""
        candidates = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                # 计算(nx,ny)的下一步可行数
                count = 0
                for ddx, ddy in moves:
                    nnx, nny = nx + ddx, ny + ddy
                    if is_valid(nnx, nny):
                        count += 1
                candidates.append((count, nx, ny))
        # 按可行数升序排序，优先尝试分支少的位置
        candidates.sort()
        return [(nx, ny) for _, nx, ny in candidates]
    def dfs(x, y, step):
        """DFS搜索路径"""
        if step == n * n:  # 终止条件：所有格子已访问
            return True
        for nx, ny in get_next_moves(x, y):  # 按优化顺序尝试下一步
            board[nx][ny] = step  # 标记访问
            if dfs(nx, ny, step + 1):  # 递归
                return True
            board[nx][ny] = -1  # 回溯
        return False
    # 从起始位置开始搜索
    board[sr][sc] = 0
    if dfs(sr, sc, 1):
        print("success")
    else:
        print("fail")
knight_tour()