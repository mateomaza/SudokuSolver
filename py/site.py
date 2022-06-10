#Final Project: Using all the things we have learnt, create a function that solves any Sudoku

import numpy as np

unsolved_hrd = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]]

unsolved_izi = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0]]

unsolved_bgn = [[1, 0, 0, 9, 0, 4, 0, 8, 2],
                [0, 5, 2, 6, 8, 0, 3, 0, 0],
                [8, 6, 4, 2, 0, 0, 9, 1, 0],
                [0, 1, 0, 0, 4, 9, 8, 0, 6],
                [4, 9, 8, 3, 0, 0, 7, 0, 1],
                [6, 0, 7, 0, 1, 0, 0, 9, 3],
                [0, 8, 6, 0, 3, 5, 2, 0, 9],
                [5, 0, 9, 0, 0, 2, 1, 3, 0],
                [0, 3, 0, 4, 9, 7, 0, 0, 8]]


s_s = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
       [9, 6, 5, 3, 2, 7, 1, 4, 8],
       [3, 4, 1, 6, 8, 9, 7, 5, 2],
       [5, 9, 3, 4, 6, 8, 2, 7, 1],
       [4, 7, 2, 5, 1, 3, 6, 8, 9],
       [6, 1, 8, 9, 7, 2, 4, 3, 5],
       [7, 8, 6, 2, 3, 5, 9, 1, 4],
       [1, 5, 4, 7, 9, 6, 8, 2, 3],
       [2, 3, 9, 8, 4, 1, 5, 6, 7]]



def sudoku_solver(sudoku, sol):
    # Sudoku is solved (no 0s & correct order):

    import numpy as np
    check = np.all(sudoku)
    if check:
        sol += sudoku
        print("")
        print(np.matrix(sol))
        print("")
        return "Solved!"

    import numpy as np
    print(np.matrix(sudoku))
    print("")
    print("")

    # Number repeats in row:

    filtered_rows = []
    i = 0
    while i < 9:
        filtered_rows.append(list(filter(None, sudoku[i])))
        i += 1
    num_rows = len(filtered_rows)
    for n in range(num_rows):
        if len(filtered_rows[n]) > len(set(filtered_rows[n])):
            return None


    # Number repeats in column:

    each_col = [list(i) for i in zip(*sudoku)]
    filtered_cols = []
    i = 0
    while i < 9:
        filtered_cols.append(list(filter(None, each_col[i])))
        i += 1
    num_cols = len(filtered_cols)
    for s in range(num_cols):
        if len(filtered_cols[s]) > len(set(filtered_cols[s])):
            return None


    # Number repeats in box:

    i = 0
    all_box = []
    while i < 7:
        y = 0
        while y < 9:
            new_number = sudoku[y][i:i + 3]
            all_box += new_number
            y += 1
        i += 3

    each_box = [all_box[i:i + 9] for i in range(0, len(all_box), 9)]
    filtered_box = []
    i = 0
    while i < 9:
        filtered_box.append(list(filter(None, each_box[i])))
        i += 1
    num_boxes = len(filtered_box)
    for u in range(num_boxes):
        if len(filtered_box[u]) > len(set(filtered_box[u])):
            return None





    # Recursive Cases:
    """How I solved it :)
    i = 0
    while i < 9:
        y = 0
        while y < 9:
            if sudoku[i][y] == 0:
                sudoku[i][y] += 1
                sol_with_1 = sudoku_solver(sudoku, sol)
                if sol_with_1 is not None:
                    return sol_with_1
                sudoku[i][y] += 1
                sol_with_2 = sudoku_solver(sudoku, sol)
                if sol_with_2 is not None:
                    return sol_with_2
                sudoku[i][y] += 1
                sol_with_3 = sudoku_solver(sudoku, sol)
                if sol_with_3 is not None:
                    return sol_with_3
                sudoku[i][y] += 1
                sol_with_4 = sudoku_solver(sudoku, sol)
                if sol_with_4 is not None:
                    return sol_with_4
                sudoku[i][y] += 1
                sol_with_5 = sudoku_solver(sudoku, sol)
                if sol_with_5 is not None:
                    return sol_with_5
                sudoku[i][y] += 1
                sol_with_6 = sudoku_solver(sudoku, sol)
                if sol_with_6 is not None:
                    return sol_with_6
                sudoku[i][y] += 1
                sol_with_7 = sudoku_solver(sudoku, sol)
                if sol_with_7 is not None:
                    return sol_with_7
                sudoku[i][y] += 1
                sol_with_8 = sudoku_solver(sudoku, sol)
                if sol_with_8 is not None:
                    return sol_with_8
                sudoku[i][y] += 1
                sol_with_9 = sudoku_solver(sudoku, sol)
                if sol_with_9 is not None:
                    return sol_with_9
                sudoku[i][y] = 0
                return
            y += 1
        i += 1"""

    # Cleaner code, using a for loop in range(1, 10) to iterate through 1 to 9
    
    for i in range(9):
        for y in range(9):
            if sudoku[i][y] == 0:
                for n in range(1, 10):
                    sudoku[i][y] = n
                    new_sol = sudoku_solver(sudoku, sol)
                    if new_sol is not None:
                        return new_sol
                    sudoku[i][y] = 0
                return



    # No solution:
    return "No Solution"


print(sudoku_solver(unsolved_bgn, []))