from pprint import pprint


def nth_fibonacci(n: int):
    x_1 = 0
    x_2 = 1
    for _ in range(n - 2):
        new = x_1 + x_2
        x_1 = x_2
        x_2 = new
    return x_2


def nth_fibonacci_recursion(n: int):  # 3
    if n in (0, 1):
        return n

    return nth_fibonacci_recursion(n - 1) + nth_fibonacci_recursion(n - 2)


# 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_generator(n: int):
    for number in range(1, n):
        yield number


gen = factorial_generator(5)


# 1 - (n = 5)  - 5 * 24
# 2 - (n = 4)  - 4 * 6
# 3 - (n = 3)  - 3 * 2
# 4 - (n = 2)  - 2 * 1
# 5 - (n = 1)  - 1

# print(factorial(5))


# print(nth_fibonacci_recursion(6))


# 1 Lari
#
def coins_recursion_problem(price: int, coins_: list, amount_: int):
    all_variations = []

    def get_min_coins(amount: int, coins: list, coins_given: list):
        if amount == 0:
            all_variations.append(coins_given)
            return
        if len(coins) == 0:
            return
        if amount < 0:
            return

        for coin in coins:
            new_coins = coins.copy()
            new_coins.remove(coin)
            new_coins_given = coins_given.copy()
            new_coins_given.append(coin)
            get_min_coins(amount=amount - coin, coins=new_coins, coins_given=new_coins_given)

    get_min_coins(amount=amount_ - price, coins=coins_, coins_given=[])

    all_variations = sorted(all_variations, key=len)
    return all_variations[0]


# print(coins_recursion_problem(price=117, coins_=[50, 50, 50, 60, 120, 20, 11, 11, 2, 4, 6, 1, 1], amount_=200))

"""
1. Tower of Hanoi
The Tower of Hanoi is a classic problem that involves moving a stack of disks from 
one peg to another, with the constraint that you can only move one disk at a time 
and a larger disk cannot be placed on top of a smaller disk.
"""


def hanoi_tower(n, source, target, aux):
    if n == 1:
        print(f'Moving disk 1 from {source} to {target}.')
        return

    hanoi_tower(n - 1, source, aux, target)
    print(f'Moving disk {n} from {source} to {target}')
    hanoi_tower(n - 1, aux, target, source)


# hanoi_tower(3, 'A', 'C', 'B')

"""
2. Permutations of a String
Given a string, write a recursive function to print all permutations of the characters in the string. 
The permutations can be printed in any order.
: Generate all permutations of a given string.
"""


def all_permutations(s_lst, l_idx, r_idx):
    if l_idx == r_idx:
        print(''.join(s_lst))
        return
    for index in range(l_idx, r_idx + 1):
        s_lst[l_idx], s_lst[index] = s_lst[index], s_lst[l_idx]
        all_permutations(s_lst, l_idx + 1, r_idx)
        s_lst[l_idx], s_lst[index] = s_lst[index], s_lst[l_idx]


def all_permutations_without_lst(chars: str, new_str: str):
    if len(chars) == 0:
        print(new_str)
        return

    for index in range(len(chars)):
        new_char = chars[index]
        all_permutations_without_lst(chars[:index] + chars[index + 1:], new_str + new_char)


s = 'ABC'


# all_permutations_without_lst(s, '')


def all_permutations_with_repetitions(chars: str, new_str: str):
    if len(chars) == len(new_str):
        print(new_str)
        return

    for index in range(len(chars)):
        new_char = chars[index]
        all_permutations_with_repetitions(chars, new_str + new_char)


# all_permutations_with_repetitions(s, '')
# all_permutations(list(s), 0, len(s) - 1)


"""
3. N-Queens Problem
The N-Queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten 
each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.
: Write a recursive solution to the N-Queens problem.
"""


def n_queens_problem(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    # TODO: CHANGE
    def is_safe(row, col):
        for idx in range(len(board[row])):
            if board[row][idx] == 'Q':
                return False
        for idx in range(len(board[row])):
            if board[idx][col] == 'Q':
                return False

        # Check upper diagonal on left side
        for idx, jdx in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[idx][jdx] == 'Q':
                return False

        # Check lower diagonal on left side
        for idx, jdx in zip(range(row, len(board), 1), range(col, -1, -1)):
            if board[idx][jdx] == 'Q':
                return False

        return True

    def print_board():
        temp = []
        for row in range(len(board)):
            output = [' '.join(board[row])]
            temp.append(output)
        solutions.append(temp)

    def solve(row):
        if row == n:
            print_board()
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'

    solve(0)

    for elem in solutions:
        for row in range(len(elem)):
            print(elem[row])
        print(end='\n\n')


# n_queens_problem(4)


"""
4. Subset Sum Problem
Given a set of integers and a target sum, determine if there is a subset 
of the given set with a sum equal to the given sum.
: Find a subset of a given set of integers that sum up to a given sum.
"""


def subset_sum(numbers: list, target: int, result: list, l_idx: int):
    if target == 0:
        print(result)
        return

    if target < 0 or l_idx == len(numbers):
        return

    subset_sum(numbers, target - numbers[l_idx], result + [numbers[l_idx]], l_idx + 1)
    subset_sum(numbers, target, result, l_idx + 1)


# subset_sum([3, 34, 4, 12, 5, 2], 9, [], 0)

"""
5. Rat in a Maze
Consider a rat placed at the entrance of a maze. The maze is represented as a 2D array, 
where 0s are blocked paths and 1s are open paths. The rat can move in four directions: up, down, left, and right. 
The goal is for the rat to find a path from the entrance to the exit.
: Write a recursive solution to find a path for the rat from the entrance to the exit of the maze.
"""


def rat_in_a_maze(maze: list[list[int]], curr_row: int, curr_col: int, target_row: int, target_col: int):
    if curr_row > len(maze) - 1 or curr_row < 0 or curr_col > len(maze) - 1 or curr_col < 0:
        return

    if maze[curr_row][curr_col] in [0, -1]:
        return

    if curr_row == target_row and curr_col == target_col:
        maze[curr_row][curr_col] = -1
        for row in maze:
            print(row)
        print()

    maze[curr_row][curr_col] = -1
    rat_in_a_maze(maze, curr_row - 1, curr_col, target_row, target_col)
    rat_in_a_maze(maze, curr_row, curr_col - 1, target_row, target_col)
    rat_in_a_maze(maze, curr_row + 1, curr_col, target_row, target_col)
    rat_in_a_maze(maze, curr_row, curr_col + 1, target_row, target_col)
    maze[curr_row][curr_col] = 1


maze_ = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
]

# rat_in_a_maze(maze_, 3, 0, 0, 2)


"""
6. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
: For given n, generate all combinations of well-formed parentheses.
"""


def generate_parentheses(n_left: int, n_right: int, curr: str):
    if n_left < 0 or n_right < 0:
        return

    if n_left == 0 and n_right == 0:
        rights_needed = 0
        for ch in curr:
            if ch == '(':
                rights_needed += 1
            elif ch == ')':
                rights_needed -= 1
            if rights_needed < 0:
                return
        print(curr)

    generate_parentheses(n_left - 1, n_right, curr + '(')
    generate_parentheses(n_left, n_right - 1, curr + ')')


N = 3
# generate_parentheses(N, N, '')


"""
7. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells. 
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
: Fill the empty cells to solve the Sudoku puzzle.
"""


def check_win(board: list[list[int]]):
    n = 9

    # Check rows and columns
    for i in range(n):
        row_nums = set()
        col_nums = set()
        for j in range(n):
            # Check rows
            if board[i][j] in row_nums or not 1 <= board[i][j] <= 9:
                return False
            row_nums.add(board[i][j])

            # Check columns
            if board[j][i] in col_nums or not 1 <= board[j][i] <= 9:
                return False
            col_nums.add(board[j][i])

    # Check 3x3 sub-boxes
    for start_row in range(0, n, 3):
        for start_col in range(0, n, 3):
            box_nums = set()
            for i in range(3):
                for j in range(3):
                    val = board[start_row + i][start_col + j]
                    if val in box_nums or not 1 <= val <= 9:
                        return False
                    box_nums.add(val)

    return True


def print_sudoku_board(board: list[list[int]]):
    for row in board:
        print(row)
    print()


def get_sudoku_empty_board() -> list[list[int]]:
    lst = []
    for _ in range(9):
        lst.append([0 for _ in range(9)])
    return lst


def is_valid_move(board: list[list[int]], row: int, col: int, num) -> bool:
    n = 9
    # Check if the number is already in the row
    if num in board[row]:
        return False

    # Check if the number is already in the column
    for i in range(n):
        if board[i][col] == num:
            return False

    # Check if the number is in the 3x3 sub-box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

exec_finished = False

def sudoku_solver(board: list[list[int]], row: int, col: int, num: int):
    global exec_finished
    if exec_finished:
        return
    
    if row < 0 or col < 0 or row > 8 or col > 8:
        return

    if board[row][col] != 0:
        return

    if not (row == 0 and col == 0):
        if not is_valid_move(board, row, col, num):
            return

    board[row][col] = num

    finished = True
    for row_ in board:
        if 0 in row_:
            finished = False

    if finished:
        if check_win(board):
            exec_finished = True
            print_sudoku_board(board)
        return

    for num_ in range(1, 10):
        sudoku_solver(board, row - 1, col, num_)
        sudoku_solver(board, row, col - 1, num_)
        sudoku_solver(board, row + 1, col, num_)
        sudoku_solver(board, row, col + 1, num_)

    board[row][col] = 0


board_ = get_sudoku_empty_board()
sudoku_solver(board_, 0, 0, 1)
