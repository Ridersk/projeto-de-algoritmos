from graph import Graph, Node, Edge


def main():
    graph = Graph()
    graph.create_nodes([0, 1, 2, 3, 4, 5, 6, 7, 8])
    nodes = graph.nodes
    graph.create_relationship(nodes[0], [nodes[1]])
    graph.create_relationship(nodes[1], [nodes[2]])
    graph.create_relationship(nodes[2], [nodes[0], nodes[3]])
    graph.create_relationship(nodes[3], [nodes[4], nodes[6]])
    graph.create_relationship(nodes[4], [nodes[5]])
    graph.create_relationship(nodes[5], [nodes[3]])
    graph.create_relationship(nodes[6], [nodes[7]])
    graph.create_relationship(nodes[7], [nodes[8]])
    graph.create_relationship(nodes[8], [nodes[6]])

    graph.topological_order(nodes[2])


main()
