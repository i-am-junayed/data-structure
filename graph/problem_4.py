# Write a function hasEdge(graph, node1, node2) that checks if there is a
# direct edge between node1 and node2.

def hasEdge(graph, node1, node2):
    if node1 in graph:
      for neighbor in graph[node1]:
        if neighbor == node2:
          return True
    return False

G = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D', 'E'],
    'D': ['A', 'C', 'E', 'B'], 
    'E': ['C', 'D']
}

print(hasEdge(G, 'E', 'B')) 
