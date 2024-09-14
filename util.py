from functools import reduce
from itertools import zip_longest


def filterFirstOccurrences(array):
    transposed = list(zip(*array))
    unique_columns = [
        reduce(
            lambda acc, curr: acc + [curr] if curr not in acc else acc + [None],
            column,
            [],
        )
        for column in transposed
    ]
    result = [
        list(pair)
        for pair in zip_longest(*unique_columns)
        if all(x is not None for x in pair)
    ]
    return result
