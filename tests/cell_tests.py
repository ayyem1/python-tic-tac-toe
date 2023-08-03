import unittest

from cell import Cell
from cell_mark import CellMark

class TestCellMethods(unittest.TestCase):

    def setUp(self):
        self.testCell = Cell(0, 0, 100, 100)

    def test_cell_inits_to_empty(self):
        self.assertEqual(self.testCell.marker, CellMark.EMPTY)
    
    def test_isMarkEmpty_returns_true_for_empty(self):
        self.assertTrue(self.testCell.isMarkEmpty())

    def test_isMarkEmpty_returns_false_for_non_empty(self):
        self.testCell.mark(CellMark.X)
        self.assertFalse(self.testCell.isMarkEmpty())
    
    def test_mark_sets_correctly(self):
        result = self.testCell.mark(CellMark.O)
        self.assertTrue(result)
        self.assertEqual(self.testCell.marker, CellMark.O)

    def test_mark_does_not_override_existing_marker(self):
        result = self.testCell.mark(CellMark.X)
        self.assertTrue(result)
        self.assertEqual(self.testCell.marker, CellMark.X)

        result = self.testCell.mark(CellMark.O)
        self.assertFalse(result)
        self.assertEqual(self.testCell.marker, CellMark.X)
