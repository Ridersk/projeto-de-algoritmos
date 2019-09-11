import math


class HeapDijkstra(object):
    def __init__(self, nodes: list = []):
        '''
            structure node: (edge_lengh, destination_node, origin_node)
        '''
        self.nodes = [None]

        self.__start_heap(nodes)

    def __start_heap(self, nodes: list = []):
        for node in nodes:
            self.add_node(node)

    def show_nodes(self):
        nodes = self.nodes
        print('Heap Nodes:')
        print('[', end='')
        for index in range(1, len(nodes)):
            if index < len(nodes) - 1:
                print('(%d, %d, %d)' % (
                    nodes[index][0], nodes[index][1].value, nodes[index][2].value), end=',\n')
            else:
                print('(%d, %d, %d)' % (
                    nodes[index][0], nodes[index][1].value, nodes[index][2].value), end='')
        print(']\n')

    def add_node(self, node):
        position_index = len(self.nodes)
        self.nodes.append(node)
        self.__shift_up(node, position_index)

    def node_lenght_increment(self, node, new_origin_node, lenght_increment):
        for index in range(1, len(self.nodes)):
            if self.nodes[index] == node:
                self.nodes[index][0] += lenght_increment
                self.nodes[index][2] = new_origin_node

                self.__shift_down(node, index)
                return

    def remove_root(self):
        position_last = len(self.nodes) - 1
        position_root = 1
        if position_last <= 0:
            return
        last_node = self.nodes[position_last]

        self.nodes[position_root] = last_node
        self.nodes.pop(len(self.nodes) - 1)
        self.__shift_down(last_node, position_root)

    def __shift_up(self, node, position_node):
        position_parent = math.floor(position_node/2)
        parent_node = self.nodes[position_parent]

        if position_parent > 0 and node[0] < parent_node[0]:
            self.nodes[position_parent] = node
            self.nodes[position_node] = parent_node

            self.__shift_up(node, position_parent)

    def __shift_down(self, node, position_node):
        position_left_child = position_node * 2
        position_right_child = position_node * 2 + 1
        if position_left_child <= len(self.nodes) - 1:
            left_child_node = self.nodes[position_left_child]
        else:
            return
        if position_right_child <= len(self.nodes) - 1:
            right_child_node = self.nodes[position_right_child]
        else:
            return

        small_node = node
        position_small = position_node
        small_changed = False

        if left_child_node[0] < small_node[0]:
            small_node = left_child_node
            position_small = position_left_child
            small_changed = True
        if right_child_node[0] < small_node[0]:
            small_node = right_child_node
            position_small = position_right_child
            small_changed = True
        if small_changed:
            self.nodes[position_node] = small_node
            self.nodes[position_small] = node

            self.__shift_down(node, position_small)
