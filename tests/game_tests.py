import unittest
from cell_mark import CellMark
from game import Game

class TestGameMethods(unittest.TestCase):

    def setUp(self):
        self.game = Game((600, 600), (100, 100))

    def test_game_was_initialized_correctly(self):
        self.assertIsNotNone(self.game.gameBoard)
        self.assertIsNotNone(self.game.gameBoard)
        self.assertIsNotNone(self.game.gameBoard)

        self.assertEqual(self.game.winner, CellMark.EMPTY)
        self.assertFalse(self.game.isOver)
    
    def test_active_player_identified_correctly(self):
        self.assertEqual(self.game.getActivePlayer(), self.game.player)
        self.game.gameBoard.markCellAtIndex(0, CellMark.X)
        self.assertEqual(self.game.getActivePlayer(), self.game.opponent)
    
    def test_game_over_set_correctly_on_win(self):
        self.assertFalse(self.game.isOver)
        self.game.gameBoard.markCellAtIndex(0, CellMark.X)
        self.game.gameBoard.markCellAtIndex(1, CellMark.X)
        self.game.gameBoard.markCellAtIndex(2, CellMark.X)
        self.game.checkForGameOver()
        self.assertTrue(self.game.isOver)
    
    def test_game_over_set_correctly_on_lose(self):
        self.assertFalse(self.game.isOver)
        self.game.gameBoard.markCellAtIndex(0, CellMark.O)
        self.game.gameBoard.markCellAtIndex(1, CellMark.O)
        self.game.gameBoard.markCellAtIndex(2, CellMark.O)
        self.game.checkForGameOver()
        self.assertTrue(self.game.isOver)

    def test_game_over_set_correctly_on_draw(self):
        self.assertFalse(self.game.isOver)

        # Set up board to represent a draw
        self.game.gameBoard.markCellAtIndex(0, CellMark.X)
        self.game.gameBoard.markCellAtIndex(1, CellMark.O)
        self.game.gameBoard.markCellAtIndex(2, CellMark.X)
        self.game.gameBoard.markCellAtIndex(3, CellMark.X)
        self.game.gameBoard.markCellAtIndex(4, CellMark.O)
        self.game.gameBoard.markCellAtIndex(5, CellMark.X)
        self.game.gameBoard.markCellAtIndex(6, CellMark.O)
        self.game.gameBoard.markCellAtIndex(7, CellMark.X)
        self.game.gameBoard.markCellAtIndex(8, CellMark.O)

        self.game.checkForGameOver()
        self.assertTrue(self.game.isOver)