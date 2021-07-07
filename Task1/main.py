# Some crazy scientist created these quantum something energy cells.
# The cells are unique in a  way that they produce a stronger energy output if there are more cells next to it.
# What the scientist observed was, that the cells are aware of their cardinal direction and if you place a cell to the north,
# the energy of the cell is increased by 10% for each cell in a multiplicative manner,
# meaning if a cell has 3 cells to it’s north, you would estimate it’s power:<initial power> * 1.1 * 1.1 * 1.1
# Cells to the north, increase output by 10%
# Cells to the south, increase output by 15%
# Cells to the west, increase output by 12%
# Cells to the east, increase output by 8%

# Task 1:
# Given a grid of cells, calculate the total power.
# First line of input is the initial cell power.
# The input data will be cell counts in a single line of the grid, cells are perfectly aligned,
# so a cell placed to the top of a cell will be considered to be placed to the north respective to that cell.
# Example input:
# A power = 100 * 1.15 * 1.15
# B power = 100 * 1.1 * 1.08 * 1.15
# C power = 100 * 1.12 * 1.15
# D power = 100 * 1.1 * 1.1 * 1.08 * 1.08
# E power = 100 * 1.1 * 1.08 * 1.12
# F power = 100 * 1.12 * 1.12

# Example arrays :
# arr0 = [A]
# arr1 = [B,C]
# arr2 = [D,E,F]

# Cell A = 100 * 1.15 * 1.15 = 132.25
# Cell B = 100 * 1.15 * 1.10 * 1.08 = 136.62
# Cell C = 100 * 1.12 * 1.15 = 128.80
# Cell D = 100 * 1.10 * 1.10 * 1.08 * 1.08 = 141.1344
# Cell E = 100 * 1.1 * 1.08 * 1.12 = 133,056
# Cell F = 100 * 1.12 * 1.12 = 125,44
import time

from calculations import cell_power_calculations

# Task 1:
if __name__ == '__main__':
    start = time.time()
    print(cell_power_calculations(100, 1, 2, 3))
    print(time.time() - start)
