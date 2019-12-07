import networkx as nx

def add_planet(graph, input):
    inner = input[:input.find(')')]
    outer = input[input.find(')') + 1:]
    if (inner not in graph):
        graph.add_node(inner)
    if (outer not in graph):
        graph.add_node(outer)
    graph.add_edge(inner, outer)

def get_indirect_orbits(graph, node, ctr):
    if (len(list(graph.successors(node))) == 0):
        return (0)
    else:
        node_list = list(graph.successors(node))
        ctr += len(node_list)
        for elem in node_list:
            ctr += get_indirect_orbits(graph, elem, 0)
        return (ctr)

if __name__ == "__main__":
    G = nx.DiGraph()

    for _ in range(2306):
        input_line = input()
        add_planet(G, input_line)
    nodes = G.nodes()
    edges = G.edges()
    indirect_orbits = 0
    G = G.to_directed()
    for node in nodes:
        indirect_orbits += get_indirect_orbits(G, node, 0)
    print(indirect_orbits)
