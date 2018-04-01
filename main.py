import sys

from perceptron import Perceptron

inputFile = sys.argv[1]
outputFile = sys.argv[2]

solver = Solver()
if method == 'bfs':
    solver.bfs(initialState)
elif method == 'dfs':
    solver.dfs(initialState)
elif method == 'ast':
    solver.ast(initialState)
