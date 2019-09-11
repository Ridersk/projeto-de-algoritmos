from graph import Graph, Node, Edge
from heap import HeapDijkstra
import random


def main():
    graph = Graph()
    graph.create_nodes([0, 1, 2, 3, 4, 5, 6, 7, 8])
    nodes = graph.nodes
    graph.create_relationship(
        nodes[1], [(nodes[2], 9), (nodes[6], 14), (nodes[7], 15)])
    graph.create_relationship(nodes[2], [(nodes[3], 23)])
    graph.create_relationship(nodes[3], [(nodes[5], 2), (nodes[8], 19)])
    graph.create_relationship(nodes[4], [(nodes[3], 6), (nodes[8], 6)])
    graph.create_relationship(nodes[5], [(nodes[4], 11), (nodes[8], 16)])
    graph.create_relationship(
        nodes[6], [(nodes[3], 18), (nodes[5], 30), (nodes[7], 5)])
    graph.create_relationship(nodes[7], [(nodes[5], 20), (nodes[8], 44)])

    graph.dijkstra_algorithm(nodes[1], nodes[8])

    heap = HeapDijkstra(
        list(map(lambda node: [random.randint(0, 10), node, node], nodes)))
    heap.show_nodes()

    heap.remove_root()
    heap.show_nodes()

    heap.remove_root()
    heap.show_nodes()

    print("update node")
    heap.node_lenght_increment(heap.nodes[1], nodes[1], 15)
    heap.show_nodes()


main()
