# Given a directed graph G with N nodes. You can use any graph representation (Adjacency matrix ) to solve the 
# following problems. Write a function printSinkNodes that takes in a graph and 
# finds out the sink nodes of the given graph G.


def printSinkNodesFromMatrix(adj_matrix, node_labels):
    sink_nodes = []

    for i in range(len(adj_matrix)):
        if sum(adj_matrix[i]) == 0:
            sink_nodes.append(node_labels[i])

    if sink_nodes:
        print("Sink Node(s):", sink_nodes)
    else:
        print("No sink nodes found.")

node_labels = ['A', 'B', 'C', 'D']

adj_matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
printSinkNodesFromMatrix(adj_matrix, node_labels)
