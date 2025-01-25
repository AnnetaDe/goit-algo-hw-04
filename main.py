from array_numbers import generate_number_array
from array_strings import generate_strings_array
from compare import compare_algorithms
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timer import time_it
from sort import sort_f, sorted_f


if __name__ == "__main__":

    promt = int(input("Enter the number of elements in the array: "))
    type_of_array = int(input("Enter the type of array: 1. Numbers 2. Strings: "))

    if type_of_array == 1:
        data = generate_number_array(promt, 15151515)
        print("\n---Unsorted arrays---")
        print("Numbers: ", data)
        compare_algorithms(data)
    else:
        data = generate_strings_array(promt)
        print("\n---Unsorted arrays---")
        print("Strings: ", data)
        compare_algorithms(data)
