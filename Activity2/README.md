
# Activity 2 Question1

## Disclaimer: Assistance from GeekForgeek, YouTube videos, and Claude AI was used for this activity.
## Based on Figure 6.11 of the MCTS agent as shown in activity description
# Setup:
Make sure math, deepcopy from copy, random, time,csv, Counter from collections, and numpy
are available on your version of python

# Execution & Assumptions:
Experiment.py is the main file where MCTS agent play connect 4 and displays data.

It agent parameters are iteration cycles, child node expand_x,max_depth of the tree, exploration parameter (c),Heuristic Weight of the Tree.

Agent outputs the count moves per parameter and the average seconds for each move to be performed per parameter.

Agent outputs data into results.csv to display results of experiment.

The assumption is that the outputs would distribute the same moves on different runs in each parameter.


# Testing instructions:
Run experiment.py to run tests.
Modify: 
- columns in for loop on line 10 of experiment.py to give test values to the agent format is (column on the board from 0 to 6, player(1 or 2))
- runs variable to change how many runs you want the agent to perform
- DEFAULT and TEST variable values
view results.csv in excel or any spreadsheet application to view results of experiment run.
