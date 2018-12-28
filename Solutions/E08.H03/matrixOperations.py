def matrixPrint(M):
    for i in range(0,len(M)):
        tmp = "\t|\t"
        for j in range(0,len(M[0])):
            if (j == len(M[1])-1):
                tmp += "{0}".format(M[i][j])
            else:
                tmp += "{0}\t".format(M[i][j])
                       
        tmp += "\t|"
        print(tmp)