from insertion_sort import insertion_sort
from merge_sort import merge_sort
from run_algoritms import run_sorting_algorithm
from sort import sort_f, sorted_f
from timer import time_it

default_algorithms = {
    "Sort (In-place)": sort_f,
    "Sorted (Built-in)": sorted_f,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}


@time_it
def run_sorting_algorithm(algorithm, array):
    print("*" * 50)
    return algorithm(array)


def compare_algorithms(array: list, algorithms: dict = default_algorithms):
    """
    Compare the performance of different sorting algorithms.
    """
    time_array = []

    for name, algorithm in algorithms.items():
        copy_items = array.copy()
        sorted_items = run_sorting_algorithm(algorithm, copy_items)
        time_array.append(sorted_items[1])

        print(f"{name} Result: {sorted_items[0], "Time: ", sorted_items[1]}")

    print(
        "\n",
        "The fastest algorithm is number: ",
        time_array.index(min(time_array)) + 1,
        " with time: ",
        min(time_array),
    )
