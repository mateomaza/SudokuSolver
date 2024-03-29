#Final Project: create a function that solves a Sudoku
from flask import Flask, request, render_template
from flask_socketio import SocketIO
import numpy as np
import os
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def sudoku_solver(sudoku, sol):
  
    # Sudoku is solved (no 0s & correct order):
    check = np.all(sudoku)
    if check:
      solved_sudoku_str = np.array2string(np.matrix(sudoku), separator=', ')
      socketio.emit('sudoku_finished', {'data': solved_sudoku_str})

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
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    sudoku[i][j] = n
                    time.sleep(0.05)
                    emit_board_state(sudoku)
                    if sudoku_solver(sudoku, sol):
                        return True
                    sudoku[i][j] = 0
                return False
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    unsolved_sudoku = [[1, 0, 0, 9, 0, 4, 0, 8, 2],
                       [0, 5, 2, 6, 8, 0, 3, 0, 0],
                       [8, 6, 4, 2, 0, 0, 9, 1, 0],
                       [0, 1, 0, 0, 4, 9, 8, 0, 6],
                       [4, 9, 8, 3, 0, 0, 7, 0, 1],
                       [6, 0, 7, 0, 1, 0, 0, 9, 3],
                       [0, 8, 6, 0, 3, 5, 2, 0, 9],
                       [5, 0, 9, 0, 0, 2, 1, 3, 0],
                       [0, 3, 0, 4, 9, 7, 0, 0, 8]]
    unsolved_str = np.array2string(np.array(unsolved_sudoku), separator=', ')
    if request.method == 'POST':
        solution = sudoku_solver(unsolved_sudoku, [])
        return render_template('index.html', solution=solution, unsolved=unsolved_str)
    return render_template('index.html', unsolved=unsolved_str)

def emit_board_state(sudoku):
  new_sudoku_str = np.array2string(np.array(sudoku), separator=', ')
  socketio.emit('sudoku_step', {'data': new_sudoku_str})


@socketio.on('start_solving')
def handle_start_solving(json):
    unsolved_sudoku = [[1, 0, 0, 9, 0, 4, 0, 8, 2],
     [0, 5, 2, 6, 8, 0, 3, 0, 0],
     [8, 6, 4, 2, 0, 0, 9, 1, 0],
     [0, 1, 0, 0, 4, 9, 8, 0, 6],
     [4, 9, 8, 3, 0, 0, 7, 0, 1],
     [6, 0, 7, 0, 1, 0, 0, 9, 3],
     [0, 8, 6, 0, 3, 5, 2, 0, 9],
     [5, 0, 9, 0, 0, 2, 1, 3, 0],
     [0, 3, 0, 4, 9, 7, 0, 0, 8]]
    sudoku_solver(unsolved_sudoku, [])

if __name__ == '__main__':
   socketio.run(app, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
