class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        self.graph.setdefault(u, []).append((v, cost))

    def print_edges(self):
        for u in self.graph:
            for v, cost in self.graph[u]:
                print(f"{u} -> {v} : {cost}")

    def path_cost(self, path):
        cost = 0
        for i in range(len(path)-1):
            for v, c in self.graph.get(path[i], []):
                if v == path[i+1]:
                    cost += c
                    break
            else:
                print(f"  No edge from {path[i]} to {path[i+1]}")
                return None
        return cost

g = Graph()
g.add_edge("A", "B", 2)
g.add_edge("B", "C", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "A", 4)

g.print_edges()
print("Total:", g.path_cost(["A", "B", "C", "D"]))
print("Total:", g.path_cost(["A", "B", "C", "D", "A"]))
