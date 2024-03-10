from collections import deque,defaultdict


def Bfs(graph,start):
    Visited=set()
    queue=deque([start])
    Visited.add(start)

    while queue:
        current= queue.popleft()
        print(current,end="")

        for neighbour in graph[current]:
            if neighbour not in Visited:
                queue.append(neighbour)
                Visited.add(neighbour)

    return False

def create_graph():
    graph=defaultdict(list)
    vertices=int(input("enter no of vertices:"))

    for _ in range(vertices):
        vertex=input("enter vertex :")
        neighbiours= input("enter neighbour of above vertex:").split(",")

        graph[vertex]=neighbiours

    return graph

user_graph=create_graph()
start_node =input("enter start node:")
print("Bfs tracersal is {} ".format(start_node))
Bfs(user_graph,start_node)