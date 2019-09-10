from graph import Graph, Node, Edge


def main():
    graph = Graph()
    graph.create_nodes([0, 1, 2, 3, 4, 5, 6, 7, 8])
    node = graph.nodes
    graph.create_relationship(node[0], [node[1]])
    graph.create_relationship(node[1], [node[2]])
    graph.create_relationship(node[2], [node[0], node[3]])
    graph.create_relationship(node[3], [node[4], node[6]])
    graph.create_relationship(node[4], [node[5]])
    graph.create_relationship(node[5], [node[3]])
    graph.create_relationship(node[6], [node[7]])
    graph.create_relationship(node[7], [node[8]])
    graph.create_relationship(node[8], [node[6]])

    graph.topological_order(node[2])

    # print(list(map(lambda node: node.value, graph.nodes)))
    # print(node[2].get_value_neighbors())


main()
