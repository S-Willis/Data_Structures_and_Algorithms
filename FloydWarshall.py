
def fillD0(graph, D0, weightMatrix):
    # print(D0)
    for i in range(len(D0)):
        # print(i)
        for j in range(len(D0)):
            # print(j)
            if(i==j):
                D0[i][j] = 0
            elif(i!=j and graph[i][j]==0):
                D0[i][j] = 10000
            elif(i!=j and graph[i][j]==1):
                D0[i][j] = weightMatrix[i][j]
    return D0

def printMat(mat):
    dim_mat = len(mat)

    print()

    for i in range(dim_mat):
        toPrint = '['
        for j in range(dim_mat):
            if(j!=0 and j!=dim_mat):
                toPrint = toPrint + ' '
            if(mat[i][j] == 10000):
                toPrint = toPrint + 'i '
            else:
                toPrint = toPrint + str(mat[i][j])
                if(mat[i][j] < 10):
                    toPrint = toPrint + ' '
        toPrint = toPrint + ']'
        print(toPrint)

def FloydWarshall(graph,weightMatrix):
    n = len(graph)

    allDs = [[[0]*n for i in range(n)] for j in range(n+1)]

    D0 = allDs[0]

    allDs[0] = fillD0(graph, D0, weightMatrix)

    # print('Iteration [0]:')
    # printMat(allDs[0])

    for k in range(1,n+1):

        Dk = allDs[k]
        Dkm1 = allDs[k-1]

        for i in range(n):
            # if i==2: print('2!')
            for j in range(n):
                Dk[i][j] = Dkm1[i][j]
                if(Dkm1[i][k-1]+Dkm1[k-1][j] < Dk[i][j]):
                    Dk[i][j] = Dkm1[i][k-1]+Dkm1[k-1][j]

        # print('Iteration [' + str(k) + ']:')
        # printMat(Dk)
    # print(allDs)

    return allDs[len(allDs)-1]

def main():
    # graph = [[0,0,0,0,0,1],
    #          [1,0,0,0,0,0],
    #          [0,1,0,0,0,0],
    #          [0,0,1,0,1,0],
    #          [0,0,1,0,0,1],
    #          [0,0,0,1,0,0]]
    #
    # weights=[[0,0,0,0,0,7],
    #          [5,0,0,0,0,0],
    #          [0,3,0,0,0,0],
    #          [0,0,1,0,3,0],
    #          [0,0,2,0,0,1],
    #          [0,0,0,3,0,0]]

    graph = [[0,1,0,0,0,1],
             [1,0,1,0,1,0],
             [0,1,0,1,0,0],
             [0,0,1,0,1,0],
             [0,1,0,1,0,1],
             [1,0,0,0,1,0]]

    weights=[[0,8,0,0,0,3],
             [4,0,7,0,6,0],
             [0,5,0,1,0,0],
             [0,0,2,0,5,0],
             [0,9,0,7,0,2],
             [9,0,0,0,9,0]]

    # weights = [[0,4,0,0],
    #          [0,0,9,0],
    #          [67,0,0,62],
    #          [0,2,0,0]]
    #
    # graph = [[0,1,0,0],
    #          [0,0,1,0],
    #          [1,0,0,1],
    #          [0,1,0,0]]

    printMat(FloydWarshall(graph,weights))


if __name__ == '__main__':
    main()
