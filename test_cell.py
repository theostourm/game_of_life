import unittest
from cell import Cell


class TestCell(unittest.TestCase):

    def test_resurrect(self):
        """
        Testing the resurrection of a cell
        """
        cell = Cell(0)
        cell.resurrect()
        self.assertEqual(cell.status, 1)

    def test_kill(self):
        """
        Testing the killing of a cell
        """
        cell = Cell(1)
        cell.kill()
        self.assertEqual(cell.status, 0)

    def test_is_alive(self):
        """
        Testing the alive test of a cell
        """
        cell_alive = Cell(1)
        self.assertEqual(cell_alive.is_alive(), True)
        cell_dead = Cell(0)
        self.assertEqual(cell_dead.is_alive(), False)


