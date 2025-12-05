from graph import Graph

def exemplo():
    g = Graph()

    # Grafo de cidades com distâncias
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 4)
    g.add_edge("C", "D", 7)
    g.add_edge("C", "E", 1)

    print("\n--- Dijkstra a partir de A ---")
    distancias = g.dijkstra("A")
    print("\nDistâncias finais:", distancias)

if __name__ == "__main__":
    exemplo()
