from cell import Cell
from utils import random_value


class Grid:

    def __init__(self, length, width, proportion):
        """
        Creates a grid of length x width cells, randomly alive or dead around a given proportion.
        :param length: length of the grid
        :param width: width of the grid
        :param proportion: proportion of alive cells at the beginning
        """
        self.length = length
        self.width = width
        self.grid = [[Cell(random_value(proportion)) for j in range(self.width)] for i in range(self.length)]

    def show_grid(self):
        """
        Returns the grid as a double array of stings
        :return: the grid as an array
        """
        visual_grid = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(self.grid[i][j].status)
            visual_grid.append(row)
        return visual_grid

    def update_grid(self):
        """
        Updates the grid for the next generation, according to the cells to kill and resurrect
        """
        cells_to_update = self.cells_to_update()
        cells_to_kill = cells_to_update[0]
        cells_to_resurrect = cells_to_update[1]

        for indexes in cells_to_kill:
            self.grid[indexes[0]][indexes[1]].kill()

        for indexes in cells_to_resurrect:
            self.grid[indexes[0]][indexes[1]].resurrect()

    def cells_to_update(self):
        """
        Goes through the whole grid and returns the list of cells to kill and to resurrect
        :return: List of cells to kill, list of cells to resurrect
        """
        cells_to_kill = []
        cells_to_resurrect = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.check_cell(i, j) == "to kill":
                    cells_to_kill.append([i, j])
                elif self.check_cell(i, j) == "to resurrect":
                    cells_to_resurrect.append([i, j])

        return cells_to_kill, cells_to_resurrect

    def check_cell(self, i, j):
        """
        Checks if a cell is to be killed, resurrected or untouched for the next generation
        :param i: row index of the cell
        :param j: column index of the cell
        :return: a string saying if the (i, j) cell is to kill or to resurrect, returns empty string if nothing changes
        """
        res = ""

        cell = self.grid[i][j]

        if cell.is_alive():
            if self.count_alive_neighbours(i, j) != 2 and self.count_alive_neighbours(i, j) != 3:
                res = "to kill"
        else:
            if self.count_alive_neighbours(i, j) == 3:
                res = "to resurrect"

        return res

    def count_alive_neighbours(self, i, j):
        """
        Given a cell, counts how many of its neighbour cells are alive
        :param i: row index of the cell
        :param j: column index of the cell
        :return: number of alive neighbours of the (i, j) cell
        """
        alive_neighbours = 0

        for k in range(i-1, i+2):
            for p in range(j-1, j+2):
                if k == i and p == j:
                    pass
                elif k == -1 or p == -1 or k == self.length or p == self.width:
                    pass
                elif self.grid[k][p].is_alive():
                    alive_neighbours += 1

        return alive_neighbours
