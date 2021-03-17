from collections import deque


class Graph:
    def __init__(self, num_vertices, ):
        self._num_vertices = num_vertices # 图顶点的个数
        self._adjacency = [[] for _ in range(num_vertices)] # 临接表

    def add_edge(self, s, t):
        """
        s: 起点顶点编号
        t: 终点顶点编号
        """
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s, t, prev):
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s, t):
        """
        s: 起点顶点编号
        t: 终点顶点编号
        """
        if t == s : return

        # visited: 记录已经被访问的顶点，用来避免顶点被重复访问
        visited = [False] * self._num_vertices
        visited[s] = True
        # q: 是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点
        q = deque()
        q.append(s)
        # prev: 用来记录搜索路径。prev[w]存储的是，顶点 w 是从哪个前驱顶点遍历过来的。
        prev = [None] * self._num_vertices

        while q:
            v = q.popleft() # 已经被访问、但相连的顶点还没有被访问的顶点
            for neighbour in self._adjacency[v]: # 访问相连的顶点
                if not visited[neighbour]:
                    prev[neighbour] = v
                    if neighbour == t:
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    q.append(neighbour)
    
    def dfs(self, s, t):
        """
        s: 起点顶点编号
        t: 终点顶点编号
        """
        if t == s : return

        # visited: 记录已经被访问的顶点，用来避免顶点被重复访问
        visited = [False] * self._num_vertices
        visited[s] = True

        # prev: 用来记录搜索路径。prev[w]存储的是，顶点 w 是从哪个前驱顶点遍历过来的。
        prev = [None] * self._num_vertices
        
        # 停止递归的标志
        found = False 

        def _dfs(start):
            nonlocal found
            if found: return
            visited[start] = True
            if start == t:
                found = True
                return
            for neighbour in self._adjacency[start]:
                if not visited[neighbour]:
                    prev[neighbour] = start
                    _dfs(neighbour)
        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))

if __name__ == "__main__":
    
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 6)
    graph.dfs(0, 6)