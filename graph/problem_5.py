# Write a function hasSelfLoop(graph, node) that checks if a given node has a self-loop.

def hasSelfLoop(graph, node):
    if node in graph:
        for neighbor in graph[node]:
            if neighbor == node:
                return True
    return False

G = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'B'],
    'C': ['A', 'D', 'E'],
    'D': ['A', 'C', 'E', 'B'], 
    'E': ['C', 'D']
}

print(hasSelfLoop(G, 'A')) # False
print(hasSelfLoop(G, 'B')) # True
