# Graph Adjacency List
graph = {
    'v1': ['v2', 'v3', 'v4', 'v5'],
    'v2': ['v1', 'v4', 'v5'],
    'v3': ['v1', 'v4', 'v6'],
    'v4': ['v1', 'v2', 'v3', 'v5', 'v6', 'v7'],
    'v5': ['v1', 'v2', 'v4', 'v7'],
    'v6': ['v3', 'v4'],
    'v7': ['v4', 'v5']
}

# Available colors
colors = ['Red', 'Green', 'Blue', 'Yellow']

# Result dictionary to store assigned colors
result = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def graph_coloring(nodes, idx=0):
    if idx == len(nodes):
        return True
    
    node = nodes[idx]
    for color in colors:
        if is_safe(node, color):
            result[node] = color
            if graph_coloring(nodes, idx + 1):
                return True
            # backtrack
            result[node] = None
    return False

# Driver code
nodes = list(graph.keys())

if graph_coloring(nodes):
    print("Coloring solution:")
    for node in nodes:
        print(f"{node} -> {result[node]}")
else:
    print("No valid coloring found.")
