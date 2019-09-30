adj = [[0 for col in range(7)] for row in range(7)]
dfs_num = ['unvisited' for i in range(7)]
dfs_parent = [-1 for parent in range(7)]

def check_cycle(u):
    dfs_num[u] = 'explored'
    for v in range(len(adj[u])):
        if v is not u and adj[u][v] == 1:
            if dfs_num[v] == 'unvisited':
                dfs_parent[v] = u
                check_cycle(v)
            elif dfs_num[v] == 'explored':
                if v == dfs_parent[u]:
                    print('two ways undirected edge: %s-%s' % (v, u))
                else:
                    print('cycle: %s-%s' % (v, u))
            elif dfs_num[v] == 'visited':
                print('foward edge: %s-%s' % (u, v))
    dfs_num[v] = 'visited'

def main():
    graph_list = [0, 1, 2, 3, 4, 5, 6]

    # set adjs
    adj[0][1] = 1
    adj[1][0] = 1
    #
    adj[0][2] = 1
    adj[2][0] = 1
    # cycle
    # adj[1][2] = 1
    # adj[2][1] = 1
    #
    adj[2][3] = 1
    adj[3][2] = 1
    #
    adj[3][4] = 1
    adj[4][3] = 1
    # cycle
    # adj[4][0] = 1
    # adj[0][4] = 1

    check_cycle(0)

main()