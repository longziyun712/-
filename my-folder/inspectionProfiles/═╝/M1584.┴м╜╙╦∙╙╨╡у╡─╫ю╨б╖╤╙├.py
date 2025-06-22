class Solution:
    def minCostConnectPoints(self, points):
        graph=[]
        for i in range(len(points)):
            graph1=[]
            for j in range(len(points)):
                weight=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                graph1.append([j,weight])
            graph.append(graph1)
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
                mst_edges.append((u,v,weight))
                # 将新加入顶点的边加入堆
                for neighbor, w in graph[v]:
                    if not visited[neighbor]:
                        heapq.heappush(heap, (w, v, neighbor))
            res=0
            for _,x,y in mst_edges:
                res+=y
            return res
        return prim(graph, 0)
import ast
if __name__=='__main__':
    input_str = input()  # 例如输入: "[[0,0],[2,2],[3,10]]"
    lst = ast.literal_eval(input_str)
    print(Solution().minCostConnectPoints(lst))