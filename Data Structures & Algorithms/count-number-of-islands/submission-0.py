class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedMarksRow = [False]*len(grid[0])
        visitedMatrix = []
        for i in range(len(grid)):
            clonedArray = []
            clonedArray[:] = visitedMarksRow[:]
            visitedMatrix.append(clonedArray)
        numIslands = 0
        def dfs(i,j):
            if i >= len(grid) or i < 0:
                return 
            if j >= len(grid[0]) or j <0:
                return 
            if visitedMatrix[i][j] == True:
                return
            if grid[i][j] == '0':
                return
            if grid[i][j] == '1':
                visitedMatrix[i][j] = True
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
                return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visitedMatrix[i][j] == False and grid[i][j] == '1':
                    numIslands+=1
                    dfs(i,j)
        return numIslands
        