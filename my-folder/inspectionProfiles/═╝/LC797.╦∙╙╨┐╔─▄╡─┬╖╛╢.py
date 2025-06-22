class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(node, path, visited):
            if node == len(graph) - 1:  # 到达终点
                res.append(path.copy())  # 注意要用copy()
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # 标记已访问
                    path.append(neighbor)  # 加入路径
                    dfs(neighbor, path, visited)  # 递归
                    path.pop()  # 回溯
                    visited.remove(neighbor)  # 撤销标记

        res = []
        dfs(0, [0], set([0]))
        return res
