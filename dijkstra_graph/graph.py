from copy import deepcopy
import random


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

        for neighbor in neighbors:
            edge = self.__make_edge(node, neighbor)
            node.add_neighbor(neighbor, edge)
            # neighbor.add_neighbor(node, edge)
            self.edges.append(edge)

        return neighbors

    def __make_edge(self, node, neighbor):
        edge = Edge()
        edge.node_start = node
        edge.node_end = neighbor[0]
        edge.length = neighbor[1]
        return edge

    def dijkstra_bfs(self, initial_node):
        queue = []

        def enqueue(node):
            node.visited = True
            queue.append(node)

        def dequeue():
            queue[0].active = False
            queue[0].topological_count = 0
            return queue.pop(0)

        if initial_node.active:
            enqueue(initial_node)

        while len(queue) > 0:
            current_node = dequeue()
            print(current_node.value)
            for neighbor in current_node.neighbors:
                if not neighbor.node.visited and neighbor.node.active:
                    enqueue(neighbor.node)

    def reverse(self, nodes):
        for node in nodes:
            while len(node.neighbors) > 0:
                neighbor = node.neighbors[0]
                if not neighbor.edge.isReverse:
                    neighbor.node.add_neighbor(node, neighbor.edge)
                    neighbor.edge.isReverse = True
                    node.remove_neighbor(neighbor)
                else:
                    break
        return nodes

    def clear_visited_nodes(self, nodes):
        for node in nodes:
            node.visited = False
        return nodes

    def dijkstra_algorithm(self, initial_node, end_node):
        '''
            Algoritmo dijkstra de menor caminho em grafos com pesos
        '''

        # proteger a estrutura original
        graph_nodes = deepcopy(self.nodes)
        first_node = graph_nodes[initial_node.value]
