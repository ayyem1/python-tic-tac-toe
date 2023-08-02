import random
from cell_mark import CellMark
from game_board import GameBoard
from player import Player

"""
Represents a player whose moves are controlled via a decision tree.
"""
class AIPlayer(Player):
    """
    This method implements the AI's move. There are two options, naive and expert. You can enable whichever you'd like to play.
    @returns bool True if the move was successfully executed, false otherwise.
    """
    def doMove(self, gameBoard: GameBoard) -> bool:
        #return self.doNaiveMove(gameBoard)
        return self.doExpertMove(gameBoard)
    
    """
    This method will select a random cell from the remaining empty cells,
    and mark it.
    @returns bool True if the move was successfully executed, false otherwise.
    """
    def doNaiveMove(self, gameBoard: GameBoard) -> bool:
        availableCells = gameBoard.getAllCellsWithMark(CellMark.EMPTY)
        if len(availableCells) == 0:
            return False
        
        return gameBoard.markCellAtIndex(random.choice(range(len(availableCells))), self.playerMarker)
    
    """
    This method will use the minmax algorithm to determine the best possible move to take.
    @returns bool True if the move was successfully executed, false otherwise.
    """
    def doExpertMove(self, gameBoard: GameBoard) -> bool:
        moveScorePairs = []
        # Simulate first level for simplicity and let simulateMinMax() handle the rest.
        for i in range(len(gameBoard.cells)):
            if not gameBoard.cells[i].isMarkEmpty(): continue
            simulatedBoard = self.createBoardWithSimulatedMove(gameBoard, i)
            moveScorePairs.append((i, self.simulateMinMax(simulatedBoard, 1)))

        if len(moveScorePairs) == 0: return False

        movesSortedByCost = sorted(moveScorePairs, key=lambda item: item[1][1])
        bestMove = min(movesSortedByCost, key=lambda item: item[1][0])
        return gameBoard.markCellAtIndex(bestMove[0], self.playerMarker)
    
    """
    Creates a deep copy of the given gameBoard and marks the cell specified by cellIndex in the copy.
    @return deep copy of gameBoard with cellIndex marked based on whoever the active player is in the simulation.
    """
    def createBoardWithSimulatedMove(self, gameBoard: GameBoard, cellIndex: int) -> GameBoard:
        # Create a copy of the game board so we don't overwrite the real one.
        copiedBoard = GameBoard(gameBoard.gridSize, gameBoard.padding)
        copiedBoard.reset()
        for i in range(len(gameBoard.cells)):
            copiedBoard.cells[i].mark(gameBoard.cells[i].marker)

        activeMarker = copiedBoard.getLesserMark()
        copiedBoard.markCellAtIndex(cellIndex, activeMarker)
        return copiedBoard
    
    """
    Utility function that simulates the minmax starting at level 1. This function will recurse until it reaches an end condition. See grade().
    @returns tuple where the first element is the grade for the given board and the second element is the cost it took to get to there.
    """
    def simulateMinMax(self, gameBoard: GameBoard, cost: int) -> tuple[int]:
        boardGrade = self.grade(gameBoard)
        if boardGrade != None:
            return (boardGrade, cost)
        
        scoreCostPairs = []
        for i in range(len(gameBoard.cells)):
            if not gameBoard.cells[i].isMarkEmpty(): continue
            simulatedBoard = self.createBoardWithSimulatedMove(gameBoard, i)
            scoreCostPairs.append(self.simulateMinMax(simulatedBoard, cost + 1))
        
        best = scoreCostPairs[0]
        currentMarker = gameBoard.getLesserMark()
        # Calculate min score for AI
        if currentMarker == self.playerMarker:
            for pair in scoreCostPairs:
                if pair[0] < best[0]:
                    best = pair
        # Calculate max score for Player
        else:
            for pair in scoreCostPairs:
                if pair[0] > best[0]:
                    best = pair

        return best
    
    """
    @returns a nullable score based on the given board. None will be returned if there is no winner, 0 if there is a draw, 10 if the player wins, -10 if the AI wins.
    """
    def grade(self, gameBoard: GameBoard) -> int:
        winner = gameBoard.getWinner()
        isDraw = gameBoard.isBoardFilled() and winner == None
        if isDraw:
            return 0
        elif winner == self.playerMarker:
            return -10 # AI is trying to minimize score
        elif winner != None:
            return 10 # Player will try to maximize score
        else:
            return None