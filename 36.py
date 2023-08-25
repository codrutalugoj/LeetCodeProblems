# https://leetcode.com/problems/valid-sudoku/
import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # make hashmaps (dictionaries) for rows, cols and boxes
        # dictionaries of sets to detect dupes

        rows = collections.defaultdict(set) # keys are row nums
        cols = collections.defaultdict(set) # keys are col nums
        boxes = collections.defaultdict(set) # keys are row/3, col/3

        for i in range(len(board)):
            for j in range(len(board)):
                # check first if there's something at that cell
                if board[i][j] == ".":
                    continue
                # if we have a dupe, the Sudoku isn't valid
                if ((board[i][j] in rows[i]) or 
                    (board[i][j] in cols[j]) or 
                    (board[i][j] in boxes[(i // 3, j // 3)])):
                    return False
                # update the hashmaps with the new digit we encountered
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3, j // 3)].add(board[i][j])
        return True 