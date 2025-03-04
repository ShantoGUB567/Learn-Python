from collections import deque

# Graph from the given picture (with adjacency list order tweaked)
graph = {
    0: [2, 1],   # Visit node 2 first, then node 1
    1: [2],      # Node 1 points to Node 2
    2: [3],      # Node 2 points to Node 3
    3: [4],      # Node 3 points to Node 4
    4: [5],      # Node 4 points to Node 5
    5: []        # Node 5 has no outgoing edges
}

def bfs_traversal(start_node):
    visited = set()
    queue = deque([start_node])
    bfs_order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

# Perform BFS starting from node 0
bfs_result = bfs_traversal(0)
print("BFS Traversal Order:", bfs_result)
