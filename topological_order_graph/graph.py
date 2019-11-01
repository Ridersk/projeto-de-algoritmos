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

    def topological_dfs(self, initial_node: Node, graph_nodes: list):
        count = [0]
        last_node = self.__depth_first_search(initial_node, count)

        #  restante dos nodes nao visitados
        while False in list(map(lambda node: node.visited, graph_nodes)):
            for node in graph_nodes:
                if node.visited == False:
                    last_node = self.__depth_first_search(
                        node, count)
                    break
        return last_node

    def __depth_first_search(self, initial_node: Node, count):
        initial_node.visited = True

        count[0] += 1

        for neighbor in initial_node.neighbors:
            if not hasattr(neighbor.node, 'visited') or neighbor.node.visited == False:
                neighbor.node.visited = True
                self.__depth_first_search(neighbor.node, count)

        count[0] += 1
        # print(initial_node.value, 'count: ', count[0])
        initial_node.topological_count = count[0]
        return initial_node

    def topological_bfs(self, initial_node):
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

    def topological_bfs_components(self, nodes):
        def node_count_bigger():
            max_count = max(
                list(map(lambda node: node.topological_count, nodes)))
            for node in nodes:
                if node.topological_count == max_count and node.active:
                    return node

        component_count = 0
        while component_count < 5 and False in list(map(lambda node: node.visited, nodes)):
            print("\nComponent %d:" % component_count)
            node = node_count_bigger()
            self.topological_bfs(node)
            component_count += 1

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

    def topological_order(self, initial_node):
        '''
            Ordenacao Topologica
        '''
        print("\t\t--- Topological Ordering Components ---\n\n")

        # proteger a estrutura original
        graph_nodes = deepcopy(self.nodes)
        first_node = graph_nodes[initial_node.value]

        # primeira etapa: dfs
        last_node = self.topological_dfs(first_node, graph_nodes)
        print("last: ", last_node.value)

        # segunda etapa: arvore inversa
        graph_nodes = self.reverse(graph_nodes)

        # terceira etapa: bfs para encontrar os componentes
        graph_nodes = self.clear_visited_nodes(graph_nodes)
        self.topological_bfs_components(graph_nodes)
