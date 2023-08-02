from enum import IntEnum
"""
Represents the three states a cell can be in throughout a game of tic-tac-toe.
"""
class CellMark(IntEnum):
    EMPTY = 0
    X = 1
    O = 2