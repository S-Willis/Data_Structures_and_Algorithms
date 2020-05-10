visited = None
vertices = None

minSpanTree = None

def dfs(graph):
    global visited, vertices

    visited = [False]*len(graph)
    vertices = list(graph.keys())

    # print(vertices)

    for i in range(len(vertices)):
        if visited[i] == False:
            dfsFromVertex(graph,i)


def dfsFromVertex(graph,i):



    global visited, vertices, minSpanTree
    visited[i] = True

    # print(vertices[i])


    adjacent = graph[vertices[i]]

    for node in range(len(adjacent)):
        if visited[vertices.index(adjacent[node])] == False:
            print(str(vertices[i]) + ' --> ' + str(vertices[vertices.index(adjacent[node])]))
            dfsFromVertex(graph,vertices.index(adjacent[node]))


if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    dfs(graph)
