import unittest
from ai_player import AIPlayer
from cell_mark import CellMark
from game_board import GameBoard


class TestAIPlayerMethods(unittest.TestCase):

    def setUp(self):
        self.gameBoard = GameBoard((600, 600), (100, 100))
        self.gameBoard.reset()

        self.aiPlayer = AIPlayer(CellMark.O)
    
    def test_do_naive_move_returns_false_for_full_board(self):
        for i in range(len(self.gameBoard.cells)):
            self.gameBoard.markCellAtIndex(i, CellMark.X)
        
        self.assertFalse(self.aiPlayer.doNaiveMove(self.gameBoard))

    def test_do_naive_move_marks_random_cell(self):
        self.assertTrue(self.aiPlayer.doNaiveMove(self.gameBoard))
        aiMarks = self.gameBoard.getAllCellsWithMark(self.aiPlayer.playerMarker)
        self.assertEqual(len(aiMarks), 1)

    def test_do_expert_move_returns_false_for_full_board(self):
        for i in range(len(self.gameBoard.cells)):
            self.gameBoard.markCellAtIndex(i, CellMark.X)
        
        self.assertFalse(self.aiPlayer.doExpertMove(self.gameBoard))
    
    # Note: This test slows down the entire unit test suite because our minmax algorithm isn't optimized.
    def test_do_expert_move_marks_upper_left_on_first_move(self):
        self.assertTrue(self.aiPlayer.doExpertMove(self.gameBoard))
        self.assertEqual(self.gameBoard.cells[0].marker, self.aiPlayer.playerMarker)
    
    def test_grade_returns_ten_on_player_win(self):
        self.gameBoard.markCellAtIndex(0, CellMark.X)
        self.gameBoard.markCellAtIndex(1, CellMark.X)
        self.gameBoard.markCellAtIndex(2, CellMark.X)
        self.assertEqual(self.aiPlayer.grade(self.gameBoard), 10)
    
    def test_grade_returns_negative_ten_on_ai_win(self):
        self.gameBoard.markCellAtIndex(0, CellMark.O)
        self.gameBoard.markCellAtIndex(1, CellMark.O)
        self.gameBoard.markCellAtIndex(2, CellMark.O)
        self.assertEqual(self.aiPlayer.grade(self.gameBoard), -10)

    def test_grade_returns_zero_on_draw(self):
        # Set up board to represent a draw
        self.gameBoard.markCellAtIndex(0, CellMark.X)
        self.gameBoard.markCellAtIndex(1, CellMark.O)
        self.gameBoard.markCellAtIndex(2, CellMark.X)
        self.gameBoard.markCellAtIndex(3, CellMark.X)
        self.gameBoard.markCellAtIndex(4, CellMark.O)
        self.gameBoard.markCellAtIndex(5, CellMark.X)
        self.gameBoard.markCellAtIndex(6, CellMark.O)
        self.gameBoard.markCellAtIndex(7, CellMark.X)
        self.gameBoard.markCellAtIndex(8, CellMark.O)

        self.assertEqual(self.aiPlayer.grade(self.gameBoard), 0)

    def test_grade_returns_none_for_no_winner(self):
        self.assertIsNone(self.aiPlayer.grade(self.gameBoard))
    
    