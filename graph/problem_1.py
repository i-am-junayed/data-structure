## Question : You are given an Adjacency Matrix of a graph. Make it an Adjacency List. 

def adjacency_matrix_to_list(adj_matrix):
    adj_list = {}
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        adj_list[i] = []
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)

    return adj_list

n = 4
node_name = ['a', 'b', 'c', 'd']
graph = [[0 for i in range(n)] for j in range(n)]
graph[0][1] = 1
graph[0][3] = 1
graph[1][0] = 1
graph[1][3] = 1
graph[2][3] = 1
graph[3][0] = 1
graph[3][1] = 1
graph[3][2] = 1


print("Adjacency Matrix\n")
for x in graph:
  print(x)


adj_list = adjacency_matrix_to_list(graph)

print("\nAdjacency List\n")
for node, connections in adj_list.items():
    print(f"Node {node}: {connections }")
