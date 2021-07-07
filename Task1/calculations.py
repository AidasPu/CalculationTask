from tools import collect_indexes_of_existing_cells


def cell_power_calculations(initial_power, *args):
    list_of_cells = []
    for arg in args:
        list_of_cells.append([initial_power] * arg)
    longest_row = len(args)
    if longest_row == 1:
        single_column_power_calc(list_of_cells)
    elif len(args) == 1:
        for row_index, row in enumerate(list_of_cells):
            row_power_increase_calc(list_of_cells, row_index, row)
    else:
        for row_index, row in enumerate(list_of_cells):
            row_power_increase_calc(list_of_cells, row_index, row)

            active_rows_in_column = []
            for column_index in range(longest_row):
                collect_indexes_of_existing_cells(list_of_cells, column_index, row_index, active_rows_in_column)
            column_power_increase_calc(active_rows_in_column, list_of_cells)

    return list_of_cells


def row_power_increase_calc(list_of_cells, row_index, row):
    '''
    Iterates through out the row and increases power dynamically depending on their position in row

            :parameter
                    list_of_cells (list): list of existing cells
                    row_index (int): index of row
                    row (list): list of cells in row
    '''

    cell_count = len(row)
    for cell_index, cell in enumerate(row):
        for position_of_multiplication in range(cell_count - 1):
            if position_of_multiplication > cell_index - 1:
                list_of_cells[row_index][cell_index] *= 1.08
            else:
                list_of_cells[row_index][cell_index] *= 1.12


def column_power_increase_calc(active_rows_in_column, list_of_cells):
    '''
    Iterates through out the column and increases power dynamically depending on their position in column

            :parameter
                    list_of_cells (list): list of existing cells
                    active_rows_in_column (list): list of indexes with existing cells of a column
    '''
    for active_row_index, active_rows in enumerate(active_rows_in_column):
        for multiplication_of_columns in range(len(active_rows_in_column) - 1):

            if multiplication_of_columns > active_row_index - 1:
                list_of_cells[active_rows[0]][active_rows[1]] *= 1.15
            else:
                list_of_cells[active_rows[0]][active_rows[1]] *= 1.10


def single_column_power_calc(list_of_cells):
    '''
    Flattens the 2d array column and iterates through to multiply the power depending on position of cell

            :parameter
                    list_of_cells (list): list of existing cells
    '''
    flatten_list = [[index, value] for index, row in enumerate(list_of_cells) for value in row]
    for row in flatten_list:
        for multiplication in range(len(flatten_list) - 1):
            if multiplication > row[0] - 1:
                list_of_cells[row[0]][0] *= 1.15
            else:
                list_of_cells[row[0]][0] *= 1.10
