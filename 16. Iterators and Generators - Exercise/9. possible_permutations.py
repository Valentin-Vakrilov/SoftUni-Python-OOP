from itertools import permutations


def possible_permutations(sequence):
    for element in permutations(sequence):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
