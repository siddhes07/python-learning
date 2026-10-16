
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num == ".":
                continue

            box_index = (i // 3) * 3 + (j // 3)

            if (num in rows[i] or
                num in cols[j] or
                num in boxes[box_index]):
                return False

            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)

    return True


board = []

print("Enter the Sudoku board row by row:")
print("Enter 9 characters per row, using '.' for empty cells.")

for i in range(9):
    row = input(f"Row {i + 1}: ").split()
    
    # Accept either space-separated or continuous digits
    if len(row) == 1 and len(row[0]) == 9:
        row = list(row[0])

    board.append(row)

if isValidSudoku(board):
    print("Valid Sudoku")
else:
    print("Invalid Sudoku")
