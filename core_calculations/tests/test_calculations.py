from unittest import TestCase

import numpy

from core_calculations.calculations import cell_power_calculations


class TestCellPowerCalculations(TestCase):
    initial_power = 100

    def test_cell_power_calculations(self):
        row1, row2, row3 = 100, 110, 111
        result = cell_power_calculations(self.initial_power, row1, row2, row3)
        expected_case = numpy.array([[132.25, 0., 0.], [136.62, 128.8, 0.], [141.1344, 133.056, 125.44]])
        self.assertEqual(result.all(), expected_case.all())

    def test_cell_power_calculations_single_column(self):
        row1, row2, row3, row4 = 1, 1, 0, 1
        result = cell_power_calculations(self.initial_power, row1, row2, row3, row4)
        expected_case = numpy.array([[132.25], [126.5], [0.], [121.]])
        self.assertEqual(result.all(), expected_case.all())

    def test_cell_power_calculations_single_row(self):
        row1 = 1001001
        result = cell_power_calculations(self.initial_power, row1)
        expected = numpy.array([116.64, 0., 0., 120.96, 0., 0., 125.44])
        self.assertEqual(result.all(), expected.all())
