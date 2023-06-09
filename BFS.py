Graph = {
    'A' : ['B' , 'C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
queue = []

def bfs(visited , Graph, node):
    visited.append(node)
    queue.append(node)

    while queue :
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in Graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS order : ")
bfs(visited, Graph, 'A')