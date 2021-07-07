def create_matrix_for_calculations(args, list_of_cells, initial_power):
    '''
        sets values to cells depending if cell should exist or not by using args as row indexes

                :parameter
                        args (list): a list of rows.
                        list_of_cells (int): matrix of cells.
                        initial_power (int)/(float): initial power that should be set for cell that exists.
    '''

    for row_index, arg in enumerate(args):
        converted = str(arg)
        for column_index, number in enumerate(converted):
            if int(number) == 1:
                list_of_cells[row_index][column_index] = initial_power
