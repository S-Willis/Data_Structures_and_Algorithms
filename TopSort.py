state = None
linkList = []
vertices = None

#[w w w w w]
#[A B C D E]
def printList(list):
    list.reverse()
    print(list)

def topSort(graph):
    global state, vertices
    state = ['White']*len(graph)
    for i in range(len(graph)):
        if state[i]=='White':
            sortFromVertex(graph,i)
    printList(linkList)

def sortFromVertex(graph, index):
    global state
    global linkList
    global vertices

    state[index] = 'Grey'
    #Vertices list???
    for j in range(len(graph[vertices[index]])):
        w = vertices.index(graph[vertices[index]][j])
        if state[w] == 'White':
            sortFromVertex(graph,w)
        elif state[w] == 'Grey':
            print("Graph has a cycle!")
            break
    state[index] = 'Black'
    linkList.append(vertices[index])

def main():

    global vertices

    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['C'],
    #          'E': ['F'],
    #          'F': ['C']}

    graph = { 'A': ['B','C','D'],
              'B': [],
              'C': ['E','F'],
              'D': ['G'],
              'E': [],
              'F': [],
              'G': [] }

    vertices = list(graph.keys())

    topSort(graph)

if __name__ == "__main__":
    main()
