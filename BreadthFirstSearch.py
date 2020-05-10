from Queue import *

visited = None
q = None
vertices = None

def bfs(graph):
    global visited, q, vertices
    visited = [False]*len(graph)
    q = Queue()
    vertices = list(graph.keys())
    for i in range(len(vertices)):
        if visited[i] == False:
            bfsFromVertex(graph,i)

def bfsFromVertex(graph,index):
    vertex = vertices[index]
    visited[index] = True
    q.enqueue(vertex)
    while(q.queue != []):
        adjacent = graph[vertices[index]]
        for j in range(len(adjacent)):
            if visited[vertices.index(adjacent[j])] == False:
                visited[vertices.index(adjacent[j])] = True
                q.enqueue(adjacent[j])

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    bfs(graph)
    print(visited)
    print(q.queue)
    print(vertices)
