## Given an adjacency list representation of an undirected graph, write a program to find the maximum degree of in the graph


def findMaxDegreeNode(G):
    max_degree = 0
    max_nodes = []


    for node in G:
 
      degree = len(G[node])

      if degree > max_degree:
            max_degree = degree
            max_nodes = [node]
      elif degree == max_degree:
            max_nodes.append(node)

    print("Maximum Degree:", max_degree)
    print("Node(s) with maximum degree:", max_nodes)


G = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', "D"],
    'D': ['B']
}

findMaxDegreeNode(G)
