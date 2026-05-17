class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = []
        for i in range(len(board)):
            visited.append([])
            for j in range(len(board[0])):
                visited[i].append(0)
            
        def dfs(i,j,k):
            if  i == len(board) or j == len(board[i]) or i < 0 or j < 0:
                return False
            elif  board[i][j] != word[k]:
                return False
            elif visited[i][j]:
                return False
            else:
                if board[i][j] == word[k] and k ==len(word)-1:
                    print(board[i][j],i,j)
                    return True
                res = False
                print(word[k],i,j)
                for delx,dely in directions:
                    visited[i][j] = True
                    res = res or dfs(i+delx,j+dely,k+1)
                    visited[i][j] = False
                return res
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or dfs(i,j,0)
        return res
        