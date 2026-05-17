class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        memo = []
        for i in range(len(matrix)):
            memo.append([])
            for j in range(len(matrix[0])):
                memo[i].append(False)
        counter = 0
        maxI =  len(matrix)-1
        maxJ = len(matrix[0])-1
        minI = 0 
        minJ = 0
        iFlag = True
        jFlag = True
        if len(matrix) == 1:
            return matrix[0]
        while counter < len(matrix)*len(matrix[0]):
            if counter%2:
                if jFlag:
                    for i in range(maxI+1):
                        if maxJ >= len(memo[i]) or maxJ < 0:
                            break
                        if memo[i][maxJ] == True:
                            continue
                        memo[i][maxJ] = True
                        output.append(matrix[i][maxJ])
                    jFlag = False
                    maxJ-=1
                else:
                    for i in range(maxI,minI-1,-1):
                        if minJ >= len(memo[i]):
                            break
                        if memo[i][minJ] == True:
                            continue
                        memo[i][minJ] = True
                        output.append(matrix[i][minJ])
                    jFlag = True
                    minJ+=1
            else:
                if iFlag:
                    for j in range(maxJ+1):
                        print(minI,len(memo))
                        if minI >= len(memo) or j==len(memo[minI]):
                            break
                        if memo[minI][j] == True:
                            continue
                        memo[minI][j]= True
                        output.append(matrix[minI][j])
                    iFlag = False
                    minI+=1
                else:
                    for j in range(maxJ,minJ-1,-1):
                        if maxI >= len(memo) or maxI < 0 :
                            break
                        if memo[maxI][j]== True:
                            continue
                        memo[maxI][j] = True
                        output.append(matrix[maxI][j])
                    iFlag= True
                    maxI-=1
            counter+=1
        
        return output
        