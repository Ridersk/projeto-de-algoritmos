from copy import deepcopy
import random


class Node(object):

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

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

    def create_nodes(self, values=[]):
        nodes = []
        for value in values:
            nodes.append(Node(value))
        self.nodes.extend(nodes)
        return nodes

    def create_relationship(self, node, nodes: list):
        neighbors = nodes

        for neighbor in neighbors:
            edge = self.__make_edge(node, neighbor)
            node.add_neighbor(neighbor, edge)
            # neighbor.add_neighbor(node, edge)
            self.edges.append(edge)

        return neighbors

    def __make_edge(self, node1, node2):
        edge = Edge()
        edge.node_start = node1
        edge.node_end = node2
        return edge

    def __depth_first_search(self, initial_node: Node, count):
        # node = deepcopy(initial_node)
        node = initial_node

        node.visited = True

        count[0] += 1
        print(node.value, 'count: ', count[0])

        for neighbor in node.neighbors:
            if not hasattr(neighbor.node, 'visited') or neighbor.node.visited == False:
                neighbor.node.visited = True
                self.__depth_first_search(neighbor.node, count)

        count[0] += 1
        print(node.value, 'count: ', count[0])

    def reverse(self, nodes):
        for node in nodes:
            while len(node.neighbors) > 0:
                neighbor = node.neighbors[0]
                if not neighbor.edge.isReverse:
                    print(node.value, ' remove ', neighbor.node.value)
                    neighbor.node.add_neighbor(node, neighbor.edge)
                    neighbor.edge.isReverse = True
                    node.remove_neighbor(neighbor)
                else:
                    break

    def topological_order(self, initial_node):
        '''
            Ordenacao Topologica
        '''
        count = [0]
        self.__depth_first_search(initial_node, count)
        # print(list(map(lambda node: node.visited, self.nodes)))

        #  restante dos nodes nao visitados
        while False in list(map(lambda node: node.visited, self.nodes)):
            for node in self.nodes:
                if node.visited == False:
                    self.__depth_first_search(node, count)
                    break
