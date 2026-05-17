class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        output = []
        memo = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            output.append([])
            memo.append([])
            for j in range(len(grid[i])):
                output[i].append(False)
                memo[i].append(2147483647)
        def traverseIsland(i,j):
            point = deque([(i,j)])
            output = [[False] * len(grid[0]) for _ in range(len(grid))]
            output[i][j] = True
            steps = 0
            while point:
                for _ in range(len(point)):
                    currleft,currright = point.popleft()
                    if grid[currleft][currright] == 0:
                            return steps
                    for dirleft,dirright in directions:
                        inlf= currleft+dirleft
                        inr=currright+dirright
                        
                        if (inlf < len(grid) and inr < len(grid[inlf]) and inlf >= 0 and inr >= 0
                            and grid[inlf][inr] != -1 and output[inlf][inr] == False):
                            output[inlf][inr] = True
                            point.append((inlf,inr))
                steps+=1
            return 2147483647
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = traverseIsland(i,j)
                    memo[i][j] = grid[i][j]
        return None

        