from core_calculations.calculations import cell_power_calculations
import time
if __name__ == "__main__":

    start = time.time()
    cell_power_calculations(100, 100, 110, 111)
    print(time.time() - start)