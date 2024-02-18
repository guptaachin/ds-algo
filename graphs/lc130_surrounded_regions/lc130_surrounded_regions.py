from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])
        global_seen_set = set()
        success = []
        for r in range(num_rows):
            for c in range(num_cols):
                if (board[r][c] == "O") and ((r,c) not in global_seen_set):
                    seen_set = set()
                    if self.replacePatchess(r,c,board, seen_set, global_seen_set):
                        self.replaceWithX(board, seen_set)
    
    def replaceWithX(self, board, seen_set):
        for s in seen_set:
            board[s[0]][s[1]] = "X"

    def replacePatchess(self, r,c, board, seen_set, global_seen_set):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return False
        if (r,c) in seen_set:
            return True
        if board[r][c] == "X":
            return True
        if board[r][c] == "O":
            seen_set.add((r,c))
            global_seen_set.add((r,c))
            left = self.replacePatchess(r,c-1, board, seen_set, global_seen_set)
            top = self.replacePatchess(r-1,c, board, seen_set, global_seen_set)
            right = self.replacePatchess(r,c+1, board, seen_set, global_seen_set)
            bottom = self.replacePatchess(r+1,c, board, seen_set, global_seen_set)
            if left and top and right and bottom:
                return True
            return False

