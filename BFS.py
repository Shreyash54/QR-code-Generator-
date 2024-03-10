from collections import deque,defaultdict
def Bfs(graph,start,target):
    visited=set()
    queue= deque([start])
    visited.add(start)

    while queue:
        current=queue.popleft()
        print(current,end=" ")
        if current ==target:
            return True

        for neighbour in graph.get(current):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node='A'
target_node='F'


print(f"BFS traversal from '{start_node}' to '{target_node}':")
if not Bfs(graph, start_node, target_node):
    print(f"No path found from '{start_node}' to '{target_node}'.")


