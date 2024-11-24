import random

# Function to print the Sudoku grid
def print_grid(grid):
    for i, row in enumerate(grid):
        print(" ".join(str(num) if num != 0 else "." for num in row))
        if i % 3 == 2 and i != 8:
            print("-" * 21)

# Function to find an empty spot (marked with 0)
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j  # row, col
    return None

# Function to check if placing a number is valid
def is_valid(grid, num, pos):
    row, col = pos

    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 subgrid
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True

# Solver function using backtracking
def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

# Function to generate a Sudoku puzzle with random prefilled values
def generate_sudoku(empty_cells):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid)  # Get a solved grid

    # Remove cells to create the puzzle
    count = empty_cells
    while count > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count -= 1
    return grid

# Function for the user to play the game
def play_sudoku(grid):
    attempts = 5  # Number of invalid attempts allowed

    while True:
        print("\nCurrent Sudoku grid:")
        print_grid(grid)

        # Check if there are any empty spots left
        if not find_empty(grid):
            print("\nCongratulations! You have completed the Sudoku puzzle.")
            return

        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))

            if grid[row][col] != 0:
                print("This cell is prefilled and cannot be changed.")
                continue

            if is_valid(grid, num, (row, col)):
                grid[row][col] = num
                print("Move accepted.")
            else:
                attempts -= 1
                print(f"Invalid move. You have {attempts} attempts left.")

            if attempts == 0:
                print("Game over! You've exhausted your invalid move attempts.")
                return

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except IndexError:
            print("Invalid input. Please enter a row and column between 0 and 8.")

# Generate a Sudoku puzzle with a user-defined number of empty cells
empty_cells = int(input("Enter the number of empty cells you want (1-81): "))
sudoku_grid = generate_sudoku(empty_cells)

# Let the user play
play_sudoku(sudoku_grid)