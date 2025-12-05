import heapq

class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))

    # Algoritmo de Dijkstra
    def dijkstra(self, start):
        dist = {v: float('inf') for v in self.adj}
        dist[start] = 0

        pq = [(0, start)]
        visited = set()

        print("\nExecutando Dijkstra:")

        while pq:
            d, u = heapq.heappop(pq)

            if u in visited:
                continue

            visited.add(u)
            print(f"Visitando {u}, custo = {d}")

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist
