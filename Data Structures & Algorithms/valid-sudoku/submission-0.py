class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        initial_set = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    row_tuple = (r, val)
                    col_tuple = (val, c)
                    box_tuple = (r // 3, c // 3, val)

                    if row_tuple in initial_set or col_tuple in initial_set or box_tuple in initial_set:
                        return False

                    initial_set.add(row_tuple)
                    initial_set.add(col_tuple)
                    initial_set.add(box_tuple)
        return True
        