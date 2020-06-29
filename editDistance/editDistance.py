# global dict={0:'match',1:'mutation',2:'insertion',3:'deletion'}

def reconstruct(a, sequenceS, sequenceT):


    sCount = len(sequenceS)-1
    tCount = len(sequenceT)-1

    b = ''
    c = ''
    mutations = 0

    while(sCount>=0 and tCount>=0):
        case = a[sCount+1][tCount+1]
        if(case==0 or case==1):
            b = b + sequenceS[sCount]
            c = c + sequenceT[tCount]
            sCount = sCount-1
            tCount = tCount-1
            if(case == 1):
                mutations = mutations + 1
        elif(case==2):
            b = b + '-'
            c = c + sequenceT[tCount]
            tCount = tCount-1
            mutations = mutations + 1
        elif(case==3):
            b = b + sequenceS[sCount]
            c = c + '-'
            sCount = sCount-1
            mutations = mutations + 1
        else:
            raise Exception("Case is not valid: " + str(case))

    if(sCount<0 and tCount>-1):
        c = c + tCount*'-'

    if(tCount<0 and sCount>-1):
        b = b + sCount*'-'

    return (b[::-1],c[::-1],mutations)

def editDistance(sequenceS, sequenceT):
    d = [[5 for x in range(len(sequenceT)+1)] for y in range(len(sequenceS)+1)]
    a = [[5 for x in range(len(sequenceT)+1)] for y in range(len(sequenceS)+1)]

    for i in range(0,len(sequenceS)+1):
        d[i][0] = i
        a[i][0] = 3
    for j in range(0,len(sequenceT)+1):
        d[0][j] = j
        a[0][j] = 2


    for k in range(1,len(sequenceS)+1):
        for l in range(1,len(sequenceT)+1):

            if(sequenceS[k-1] == sequenceT[l-1]):
                d[k][l] = d[k-1][l-1]
                a[k][l] = 0
            else:
                d[k][l] = 1 + min(d[k][l-1],d[k-1][l],d[k-1][l-1])

                if d[k][l] == 1 + d[k-1][l-1]:
                    a[k][l] = 1
                elif d[k][l] == 1 + d[k][l-1]:
                    a[k][l] = 2
                else:
                    a[k][l] = 3

    result = reconstruct(a, sequenceS, sequenceT)

    return (result[0],result[1],result[2])


if __name__ == '__main__':

    print(editDistance('ACCGGTATCCTAGGAC','ACCTATCTTAGGAC'))
