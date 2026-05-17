from numpy import zeros
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = zeros((9,9)).tolist()
        columns = zeros((9,9)).tolist()
        for i,row in enumerate(board):            
            for j,cell in enumerate(row):
                if cell =='.':
                    continue
                if rows[i][int(cell)-1] ==1:
                    print('row',i,j)
                    return False
                if columns[j][int(cell)-1] ==1:
                    print('columns',i,j)
                    return False
                if not self.checkInCell(cell,i,j,board):
                    print('cell',cell,i,j)
                    return False
                rows[i][int(cell)-1] = 1
                columns[j][int(cell)-1] = 1
        return True
    def checkInCell(self,cell,i,j,board)->bool:
        indexMapping = [1,1,1,4,4,4,7,7,7]
        board[i][j] = 0
        i = indexMapping[i]
        j = indexMapping[j]
        if (board[i-1][j] == cell or board[i][j] == cell or board[i+1][j] == cell or
           board[i-1][j-1] == cell or board[i][j-1] == cell or board[i+1][j-1] == cell or 
           board[i-1][j+1] == cell or board[i][j+1] == cell or board[i+1][j+1] == cell):
           return False
        else:
            return True 




        