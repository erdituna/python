graph1 = {
    '1' : ['2','3','4'],
    '2' : ['1','5','6'],
    '3' : ['1'],
    '4' : ['1','7','8'],
    '5' : ['2','9','10'],
    '6' : ['2'],
    '7' : ['4','11','12'],
    '8' : ['4'],
    '9' : ['5'],
    '10' : ['5'],
    '11' : ['7'],
    '12' : ['7']
}


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'4', [])
print(visited)

