# Question : Given a directed graph G with N nodes. You can use any graph representation (Adjacency list) 
# to solve the following problems. Write a function printSinkNodes that takes in a graph and finds out the 
# sink nodes of the given graph G.

def printSinkNodes(graph):
    sink_nodes = []

    for node in graph:
        degree = len(graph[node])
        if degree == 0:
            sink_nodes.append(node)

    if sink_nodes:
        print("Sink Node(s):", sink_nodes)
    else:
        print("No sink nodes found.")


G = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': [],
    'D': []
}

printSinkNodes(G)
