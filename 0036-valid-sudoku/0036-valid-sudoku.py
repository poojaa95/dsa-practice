class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            l=[]
            for ch in row:
                if ch!=".":
                    if ch in l:
                        return False
                    l.append(ch)
        for col in range(9):
            l=[]
            for row in range(9):
                if board[row][col]!=".":
                    if board[row][col] in l:
                        return False
                l.append(board[row][col])
        for r in range(0,9,3):
            for c in range(0,9,3):
                l=[]
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j]!=".":
                            if board[i][j] in l:
                                return False
                            l.append(board[i][j])
        return True