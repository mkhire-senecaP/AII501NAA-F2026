import time
import csv
from collections import Counter
import numpy as np
from activity2Q1Code import *
from connectFour import *

def make_board():
    board = np.zeros((ROWS,COLS),dtype=int)
    for c,player in [(0,1),(3,2),(6,1),(4,2),(1,1),(5,2),(3,1)]:
        drop_piece(board,c,player)
    return board

DEFAULTS = {"iterations": 500, "expand_x":4,"max_depth":4,"c":1.4,"w":0.0}

TESTS = {
    "iterations": [100, 500, 2000],
    "expand_x":   [2, 4, 7],
    "max_depth":  [2, 4, 6],
    "w":          [0.0, 0.5, 1.0],
    "c":          [0.5,1.4,3.0]
}

RUNS = 20

def run_settings(board,player,config,runs):
    moves = []
    start = time.time()
    for _ in range(runs):
        
        move = MCTS_NODE.mcts_state(board,player,config)
        moves.append(move)
        avg_time = (time.time() - start)/runs
        counts = Counter(moves)
        top_share = max(counts.values())/runs
        return avg_time,top_share,counts

position, player = make_board(), 1

with open("results1.csv", "w", newline="") as f:
    out = csv.writer(f)
    out.writerow(["parameter", "value", "move_counts", "avg_seconds"])
    for param, values in TESTS.items():
        for v in values:
            cfg = dict(DEFAULTS); cfg[param] = v
            moves, start = [], time.time()
            for _ in range(RUNS):
                moves.append(MCTS_NODE.mcts_state(position, player, **cfg))
            avg = (time.time() - start) / RUNS
            counts = dict(Counter(moves))
            print(param, v, counts, round(avg, 2))
            out.writerow([param, v, counts, round(avg, 3)])