Graph = {
    'A' : ['B' , 'C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def dfs(visited, Graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

    for neighbour in Graph[node]:
        if neighbour not in visited:
            dfs(visited, Graph, neighbour)

print("The DFS order : ")
dfs(visited, Graph, 'A')