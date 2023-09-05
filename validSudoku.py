class Solution:
    # Time Complexity : O(N ^ 2)
    # Space Complexity : O(N ^ 2)
    # take three sets to maintain an array for each row, column and box
    def isValidSudoku( board: list[list[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        print(rows)
        for row in range(N):
            for column in range(N):
                val = board[row][column] 
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                rows[row].add(val)

                if val in cols[column]:
                    return False
                cols[column].add(val)
                idx = (row // 3) * 3 + column // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
    print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))