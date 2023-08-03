import unittest
from cell_mark import CellMark
from game_board import GameBoard

class TestGameBoardMethods(unittest.TestCase):

    def setUp(self):
        self.gameBoard = GameBoard((600, 600), (100, 100))
    
    def test_game_board_inits_with_empty_cells_list(self):
        self.assertEqual(len(self.gameBoard.cells), 0)
    
    def test_game_board_reset_creates_cells(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)
    
    def test_game_board_marks_correct_cell_at_point(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        result = self.gameBoard.markCellThatCollidesWithPoint((110, 110), CellMark.X);
        
        self.assertTrue(result)
        self.assertEqual(self.gameBoard.cells[0].marker, CellMark.X)
    
    def test_game_board_marks_no_cell_for_point_out_of_bounds(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        result = self.gameBoard.markCellThatCollidesWithPoint((700, 700), CellMark.X);
        
        self.assertFalse(result)
        self.assertTrue(self.gameBoard.cells[0].isMarkEmpty())
    
    def test_game_board_marks_correct_cell_at_index(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        result = self.gameBoard.markCellAtIndex(0, CellMark.X);
        
        self.assertTrue(result)
        self.assertEqual(self.gameBoard.cells[0].marker, CellMark.X)

    def test_game_board_marks_no_cell_for_index_out_of_bounds(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        result = self.gameBoard.markCellAtIndex(10, CellMark.X);
        
        self.assertFalse(result)
        self.assertTrue(self.gameBoard.cells[0].isMarkEmpty())

    def test_game_board_identifies_no_winner_correctly(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        self.assertTrue(self.gameBoard.markCellAtIndex(0, CellMark.X))
        self.assertEqual(self.gameBoard.getWinner(), None)

    def test_game_board_identifies_winner_correctly(self):
        # columns
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([0, 1, 2], CellMark.X))
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([3, 4, 5], CellMark.X))
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([6, 7, 8], CellMark.X))

        # rows
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([0, 3, 6], CellMark.X))
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([1, 4, 7], CellMark.X))
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([2, 5, 8], CellMark.X))

        # diagonals
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([0, 4, 8], CellMark.X))
        self.assertTrue(self.wasWinnerIdentifiedCorrectly([2, 4, 6], CellMark.X))

    
    def wasWinnerIdentifiedCorrectly(self, indices: list[int], winnerMark: CellMark) -> bool:
        self.gameBoard.reset()

        for i in indices:
            if not self.gameBoard.markCellAtIndex(i, winnerMark):
                return False
        
        return self.gameBoard.getWinner() == winnerMark
    
    def test_full_board_identified_correctly(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        for i in range(len(self.gameBoard.cells)):
            self.assertTrue(self.gameBoard.markCellAtIndex(i, CellMark.X))
        
        self.assertTrue(self.gameBoard.isBoardFilled())

    def test_unfilled_board_identified_correctly(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        for i in range(len(self.gameBoard.cells) - 1):
            self.assertTrue(self.gameBoard.markCellAtIndex(i, CellMark.X))
        
        self.assertFalse(self.gameBoard.isBoardFilled())

    def test_lesser_mark_identified_correctly(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        self.assertEqual(self.gameBoard.getLesserMark(), CellMark.X)
        self.gameBoard.markCellAtIndex(0, CellMark.X)
        self.assertEqual(self.gameBoard.getLesserMark(), CellMark.O)

    def test_all_marked_cells_of_type_are_retrieved_correctly(self):
        self.gameBoard.reset()
        self.assertEqual(len(self.gameBoard.cells), self.gameBoard.DIMENSION ** 2)

        for i in range(3):
            self.assertTrue(self.gameBoard.markCellAtIndex(i, CellMark.X))

        result = self.gameBoard.getAllCellsWithMark(CellMark.X)
        self.assertEqual(len(result), 3)

        result = self.gameBoard.getAllCellsWithMark(CellMark.EMPTY)
        self.assertEqual(len(result), 6)


