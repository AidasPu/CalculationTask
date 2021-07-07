import numpy as np

from core_calculations.tools import create_matrix_for_calculations


def cell_power_calculations(initial_power, *args):
    longest_row = max([len(str(arg)) for arg in args])
    longest_column = len(args)
    list_of_cells = np.zeros((longest_column, longest_row), dtype=np.float64)
    create_matrix_for_calculations(args, list_of_cells, initial_power)

    power_increase_calc(list_of_cells, initial_power, transposed=False)
    power_increase_calc(list_of_cells, initial_power)


    return list_of_cells


def power_increase_calc(list_of_cells, initial_power, transposed=True):
    '''
    Calculation of power increase for columns and rows.
    If transposed = True it will calculate columns and if transposed = False it will calculate rows.

            :parameter
                    list_of_cells (list): list of existing cells
                    initial_power (int)/(float): initial power for each cell
                    transposed (bool): if transposed = true it will calculate column power increase and
                                          transposed = False will calculate row power increase.
    '''
    if transposed:
        row_list = list_of_cells.transpose()
    else:
        row_list = list_of_cells

    for row_index, row in enumerate(row_list):
        legal_cell_array = np.where(row >= initial_power)
        if legal_cell_array[0].size <= 1:
            pass
        else:
            cell_power_multiplication(list_of_cells, row_index, legal_cell_array, transposed)


def cell_power_multiplication(list_of_cells, row_index, existing_cell_array, transposed=False):
    '''
    Abstraction layer for cell multiplication.
    transposed flag is set to true at that point it uses column cell power multiplication algorithm configuration.
    if transposed flag is set to false it will use row cell power multiplication algorithm configuration.
            :parameter
                    list_of_cells (list): list of cells
                    row_index (int): index of row
                    existing_cell_array np.array((list)): indexes of legal cells that should be multiplied.
                    transposed (bool): flag to tell the configuration if it's column or row multiplication.
    '''
    for active_cell_index, existing_cell_index in enumerate(existing_cell_array[0]):
        left_multiplication, right_multiplication, index_pair = (
            configure_multiplication_variables(transposed, existing_cell_index, row_index))

        for multiplication in range(existing_cell_array[0].size - 1):
            if multiplication > active_cell_index - 1:
                list_of_cells[index_pair[0]][index_pair[1]] *= left_multiplication
            else:
                list_of_cells[index_pair[0]][index_pair[1]] *= right_multiplication


def configure_multiplication_variables(transposed, existing_cell_index, row_index):
    '''
    Configuration layer for multiplication.
    Configures variables depending on transposed parameter.
            :parameter
                    row_index (int): index of row
                    existing_cell_array np.array((list)): indexes of legal cells that should be multiplied.
                    transposed (bool): flag to tell the configuration if it's column or row multiplication.
    '''
    if transposed:
        left_multiplication = 1.15
        right_multiplication = 1.1
        index_pair = existing_cell_index, row_index
    else:
        left_multiplication = 1.08
        right_multiplication = 1.12
        index_pair = row_index, existing_cell_index

    return left_multiplication, right_multiplication, index_pair
