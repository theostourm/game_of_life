import unittest
from grid import Grid


class TestCell(unittest.TestCase):

    def test_init(self):
        """
        Testing the size of the created grid
        """
        grid = Grid(10, 10, 0.5)
        self.assertEqual(len(grid.grid), grid.length)
        for i in range(len(grid.grid)):
            self.assertEqual(len(grid.grid[i]), grid.width)

    def test_count_alive(self):
        """
        Testing if the number of alive neighbours is correct
        """
        grid = Grid(5, 8, 0)

        grid.grid[1][1].resurrect()
        grid.grid[0][0].resurrect()
        grid.grid[0][1].resurrect()
        grid.grid[2][2].resurrect()
        grid.grid[1][2].resurrect()
        grid.grid[0][2].resurrect()
        grid.grid[-1][-1].resurrect()
        grid.grid[0][6].resurrect()
        grid.grid[1][6].resurrect()
        grid.grid[1][7].resurrect()

        self.assertEqual(grid.count_alive_neighbours(4, 7), 0)

    def test_check_cell(self):
        """
        Testing if the condition for a cell to be killed, resurrected or untouched is correct
        """
        grid = Grid(5, 8, 0)

        grid.grid[1][1].resurrect()
        grid.grid[0][0].resurrect()
        grid.grid[0][1].resurrect()
        grid.grid[2][2].resurrect()
        grid.grid[1][2].resurrect()
        grid.grid[0][2].resurrect()

        self.assertEqual(grid.check_cell(0, 1), "to kill")
        self.assertEqual(grid.check_cell(1, 1), "to kill")
        self.assertEqual(grid.check_cell(2, 1), "to resurrect")
        self.assertEqual(grid.check_cell(1, 3), "to resurrect")
        self.assertEqual(grid.check_cell(3, 6), "")
        self.assertEqual(grid.check_cell(0, 2), "")

    def test_cells_to_update(self):
        """
        Testing if the function cells_to_update returns the right cells to kill or resurrect
        """
        grid = Grid(5, 8, 0)

        grid.grid[1][1].resurrect()
        grid.grid[0][0].resurrect()
        grid.grid[0][1].resurrect()
        grid.grid[2][2].resurrect()
        grid.grid[1][2].resurrect()
        grid.grid[0][2].resurrect()

        self.assertEqual(grid.cells_to_update(), ([[0, 1], [1, 1], [1, 2]], [[1, 0], [1, 3], [2, 1]]))

    def test_update_grid_blinker(self):
        """
        Testing the blinker pattern, a 2-step period oscillator
        """
        grid = Grid(6, 8, 0)
        grid1 = Grid(6, 8, 0)

        grid.grid[2][2].resurrect()
        grid.grid[1][2].resurrect()
        grid.grid[0][2].resurrect()

        grid1.grid[2][2].resurrect()
        grid1.grid[1][2].resurrect()
        grid1.grid[0][2].resurrect()

        grid.update_grid()
        grid.update_grid()

        self.assertEqual(grid.show_grid(), grid1.show_grid())

    def test_update_grid_toad(self):
        """
        Testing the toad pattern, a 2-step period oscillator
        """
        grid = Grid(6, 8, 0)
        grid1 = Grid(6, 8, 0)

        grid.grid[2][2].resurrect()
        grid.grid[2][3].resurrect()
        grid.grid[2][4].resurrect()
        grid.grid[3][3].resurrect()
        grid.grid[3][4].resurrect()
        grid.grid[3][5].resurrect()

        grid1.grid[2][2].resurrect()
        grid1.grid[2][3].resurrect()
        grid1.grid[2][4].resurrect()
        grid1.grid[3][3].resurrect()
        grid1.grid[3][4].resurrect()
        grid1.grid[3][5].resurrect()

        grid.update_grid()
        grid.update_grid()

        self.assertEqual(grid.show_grid(), grid1.show_grid())

    def test_update_grid_beacon(self):
        """
        Testing the beacon pattern, a 2-step period oscillator
        """
        grid = Grid(6, 8, 0)
        grid1 = Grid(6, 8, 0)

        grid.grid[1][1].resurrect()
        grid.grid[2][1].resurrect()
        grid.grid[1][2].resurrect()
        grid.grid[3][4].resurrect()
        grid.grid[4][3].resurrect()
        grid.grid[4][4].resurrect()

        grid1.grid[1][1].resurrect()
        grid1.grid[2][1].resurrect()
        grid1.grid[1][2].resurrect()
        grid1.grid[3][4].resurrect()
        grid1.grid[4][3].resurrect()
        grid1.grid[4][4].resurrect()

        grid.update_grid()
        grid.update_grid()

        self.assertEqual(grid.show_grid(), grid1.show_grid())


