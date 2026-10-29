class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for every row, column, and 3x3 in these positions. 0-2x0-2, 3-5x3-5,6-8x6-6x8
        # as long as they are all unique then its true
        #for every verification, go through collect set of numsrs and if unique then yay.
        #but does edge cases where we dont know the number affect us?
        # what is a hash set
        # in the hint, how to derive this equation? We can find the index of each square by the equation (row / 3) * 3 + (col / 3). Then we use hash set for O(1) lookups while inserting the number into its row, column and square it belongs to. We use separate hash maps for rows, columns, and squares.
        row_seen = [set() for _ in range(9)]
        col_seen = [set() for _ in range(9)]
        grid_seen = [set() for _ in range(9)]
        for row in range(1,10):
            for col in range(1,10):
                tile = board[row - 1][col - 1]
                grid = ((row - 1) // 3) * 3 + ((col - 1) // 3)
                if tile == ".":
                    continue
                if tile in grid_seen[grid]:
                    return False
                grid_seen[grid].add(tile)
                if tile in row_seen[row - 1]:
                    return False
                row_seen[row - 1].add(tile)
                if tile in col_seen[col - 1]:
                    return False
                col_seen[col - 1].add(tile)
        return True
