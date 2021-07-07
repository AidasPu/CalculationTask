# Dirty solution. Could move the column_index as key and row id's of existing cells to values to dictionary from arguments.
def collect_indexes_of_existing_cells(list_of_cells, column_index, row_index, active_rows_in_column):
    '''
    Add cells to list that exist in column.
    Example: If 2d Array is similar to ([5,10,15],[5,10][5,10,15])
    The calculation should still multiply the 15's by column even if there is a gap between row 1 and row 3

        :parameter
                list_of_cells (list): list of existing cells
                column_index (int): index of column
                row_index (int): index of row
                active_rows_in_column (list): list of indexes for existing cells in columns
    '''
    try:
        if list_of_cells[column_index][row_index]:
            active_rows_in_column.append([column_index, row_index])
    except IndexError:
        pass
