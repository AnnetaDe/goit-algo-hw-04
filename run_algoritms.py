from timer import time_it


@time_it
def run_sorting_algorithm(algorithm, array):
    print("*" * 50)
    return algorithm(array)
