from random import randint


def generate_number_array(n, max_value=1000):
    return [randint(0, max_value) for _ in range(n)]
