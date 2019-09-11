from copy import deepcopy
import random
import math
from heap import HeapDijkstra


class Node(object):

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False
        self.topological_count = 0
        self.active = True

    def add_neighbor(self, node, edge):
        '''
            Add a new node and edge as neighbor
        '''
        neighbor = type('', (), {})()
        neighbor.node = node
        neighbor.edge = edge
        self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        '''
            Remove a neighbor
        '''
        for index in range(len(self.neighbors)):
            if self.neighbors[index] == neighbor:
                self.neighbors.pop(index)
                break

    def get_value_neighbors(self):
        values = []
        for neighbor in self.neighbors:
            values.append(neighbor.node.value)
        return values


class Edge(object):
    index = 0

    def __init__(self):
        self.node_start: Node
        self.node_end: Node
        self.value = Edge.index
        self.isReverse = False
        self.length = 0
        Edge.index += 1


class Graph(object):
    '''
        Grafo DIRECIONAL
    '''

    def __init__(self):
        self.nodes = []
        self.heap_nodes = HeapDijkstra()
        self.edges = []
        self.array_nodes_posX = []
        self.array_nodes_posY = []

    def show_graph(self, nodes: list):
        for node in nodes:
            print('%d -> %s' % (node.value, node.get_value_neighbors()))

    def create_nodes(self, values=[]):
        nodes = []
        for value in values:
            nodes.append(Node(value))
        self.nodes.extend(nodes)
        return nodes

    def create_relationship(self, node, neighbors: list):
        '''
            structure of entrance neighbor: (neighbor_node, edge_lenght)
        '''

        for neighbor in neighbors:
            edge = self.__make_edge(node, neighbor[0], neighbor[1])

            node.add_neighbor(neighbor[0], edge)
            self.edges.append(edge)

        # for neighbor in node.neighbors:
        #     print(neighbor.edge.value)

        return neighbors

    def __make_edge(self, node, neighbor, length):
        edge = Edge()
        edge.node_start = node
        edge.node_end = neighbor
        edge.length = length
        return edge

    def __update_edge_neighbors(self, heap_node, heap):
        '''
            estrutura heap_node: (lengh, dest_node, origin_node)
        '''
        for neighbor in heap_node[1].neighbors:
            path_length = heap_node[0] + neighbor.edge.length
            heap.update_node_lenght(neighbor.node, heap_node[1], path_length)

    def start_heap(self, first_node, graph_nodes):
        heap_nodes = []
        for node in graph_nodes:
            if node != first_node:
                heap_nodes.append([None, node, None])
            else:
                heap_nodes.append([0, node, None])

        heap = HeapDijkstra(heap_nodes)
        return heap

    def dijkstra_algorithm(self, initial_node, end_node):
        '''
            Algoritmo dijkstra de menor caminho em grafos com pesos
        '''

        # proteger a estrutura original
        graph_nodes = deepcopy(self.nodes)
        first_node = graph_nodes[initial_node.value]
        dest_node = graph_nodes[end_node.value]

        # heap para priorizar o menor caminho
        heap = self.start_heap(first_node, graph_nodes)
        # heap.show_nodes()

        print("Caminho:")
        while True:
            heap_root = heap.get_root()
            print(heap_root[1].value, end=", ")
            if heap_root[1] == dest_node:
                break
            self.__update_edge_neighbors(heap_root, heap)
            # heap.show_nodes()
        print()

        print("shortest path: distance %s, origin %s -> end %s" %
              (heap_root[0], heap_root[2].value, heap_root[1].value))
