## Connect 4 sample code from Medium: "https://markdavidjameshalstead.medium.com/writing-a-connect-four-game-for-the-command-line-in-python-32c9a2b79e97"
## MCTS code sample from: "https://www.youtube.com/watch?v=EB-NJtNERBQ"
import math
from copy import deepcopy
import random

from connectFour import *
#from meta import Game

class MCTS_NODE:
    def __init__(self,state,parent=None,player_to_move=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.N = 0
        self.Q = 0 
        self.depth = 0 if parent is None else parent.depth + 1
        self.player_to_move = player_to_move
    
    def is_terminal(self):
        return check_win(self.state) is not None or len(legal_moves(self.state)) == 0
    
    def ucb_val(self):
        if self.N == 0:
            return 0 #add if explore == 0 else GameMeta.INF
        else:
            exploit = self.Q / self.N
            c = math.sqrt(2) # for now be sure to replace with explore value from video
            explore = c * math.sqrt(math.log(self.parent.N)/self.N)
            return exploit + explore
        
    def select(node, c, w):
        while node.children and not node.is_terminal():
           node = max(node.children, key=lambda ch: MCTS_NODE.utility(ch,c,w))
        return node
    
    def expand(node,c,max_depth):
        if node.is_terminal() or node.depth >= max_depth:
            return node
        if not node.children:
            moves = legal_moves(node.state)
            chosen = random.sample(moves, min(c,len(moves)))
            for m in chosen:
                s = node.state.copy()
                drop_piece(s,m,node.player_to_move)
                child = MCTS_NODE(s,parent=node,player_to_move=3 - node.player_to_move,move=m)
                node.children.append(child)    #def mcts_state(root_state,player):
        #root = MCTS_NODE(root_state,player,depth = 0)
      #  while i is true:
        return random.choice(node.children)
    
    def simulate(node):
        s = node.state.copy()
        p = node.player_to_move
        while not game_over(s):
            m = random.choice(legal_moves(s))
            drop_piece(s,m,p)
            p = 3 - p
        return check_win(s) or 0
    
    def backpropagate(node,winner):
        while node is not None:
            node.N += 1
            mover = 3 - node.player_to_move
            if winner == mover: node.Q += 1
            elif winner == 0: node.Q += 0.5
            node = node.parent
    
    def mcts_state(root_state, player,iterations,expand_x,max_depth,c,w):
        root = MCTS_NODE(root_state,player_to_move=player)
        i = 0
        while i < iterations:
            leaf = MCTS_NODE.select(root,c,w)
            child = MCTS_NODE.expand(leaf,expand_x,max_depth)
            result = MCTS_NODE.simulate(child)
            MCTS_NODE.backpropagate(child,result)
            i += 1
        best = max(root.children, key=lambda ch: ch.N)
        return best.move
    
    def utility(child,c,w):
        if child.N == 0:
            return float("inf")
        playout = child.Q/ child.N
        explore = c * math.sqrt(math.log(child.parent.N)/child.N)
        objective = MCTS_NODE.heuristic(child.state, child.parent.player_to_move) 
        return playout + explore + w * objective
    
    def heuristic(state, player):
        centre = state[:, COLS // 2]
        score = np.sum(centre == player) - np.sum(centre == 3 - player)
        return score / ROWS

if __name__ == "__main__":
    # Test 1: player 1 can win in column 3 (index 3)
    b = np.zeros((ROWS, COLS), dtype=int)
    b[5][0] = b[5][1] = b[5][2] = 1
    print("Win test (expect 3):", MCTS_NODE.mcts_state(b, 1, 500, 7, 4, 1.4, 0))

    # Test 2: player 2 threatens column 3, player 1 must block
    b = np.zeros((ROWS, COLS), dtype=int)
    b[5][0] = b[5][1] = b[5][2] = 2
    b[4][0] = 1
    b[4][1] = 1
    print("Block test (expect 3):", MCTS_NODE.mcts_state(b, 1, 500, 7, 4, 1.4, 0))
