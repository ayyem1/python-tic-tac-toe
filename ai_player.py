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
        #NOTE: Only one of these two lines should be enabled
        return self.doNaiveMove(gameBoard) # This line enables easy difficulty for AI
        #return self.doExpertMove(gameBoard) # This line enables hard difficulty for AI

    """
    This method will select a random cell from the remaining empty cells,
    and mark it.
    @returns bool True if the move was successfully executed, false otherwise.
    """
    def doNaiveMove(self, gameBoard: GameBoard) -> bool:
        availableCells = gameBoard.getAvailableGridIndices()
        if len(availableCells) == 0:
            return False
        
        choice = random.choice(range(len(availableCells)))
        return gameBoard.markCellAtIndex(availableCells[choice], self.playerMarker)

    """
    This method will use the minmax algorithm to determine the best possible move to take.
    @returns bool True if the move was successfully executed, false otherwise.
    """
    def doExpertMove(self, gameBoard: GameBoard) -> bool:
        moveScorePairs = []
        # Simulate first level for simplicity and let simulateMinMax() handle the rest.
        for i in range(len(gameBoard.cells)):
            if not gameBoard.cells[i].isMarkEmpty(): continue
            # Mark board with candidate move
            gameBoard.markCellAtIndex(i, gameBoard.getLesserMark())
            # Calculate score
            moveScorePairs.append((i, self.simulateMinMax(gameBoard, 1)))
            # Revert candidate move
            gameBoard.cells[i].marker = CellMark.EMPTY

        if len(moveScorePairs) == 0: return False

        movesSortedByCost = sorted(moveScorePairs, key=lambda item: item[1][1])
        bestMove = min(movesSortedByCost, key=lambda item: item[1][0])
        return gameBoard.markCellAtIndex(bestMove[0], self.playerMarker)

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
            # Mark board with candidate move
            gameBoard.markCellAtIndex(i, gameBoard.getLesserMark())
            # Calculate score
            scoreCostPairs.append(self.simulateMinMax(gameBoard, cost + 1))
            # Revert candidate move
            gameBoard.cells[i].marker = CellMark.EMPTY

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
