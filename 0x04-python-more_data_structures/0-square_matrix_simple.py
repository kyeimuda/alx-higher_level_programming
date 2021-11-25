#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for index in matrix:
        sub = []
        for index2 in index:
            r = index2 ** 2
            sub.append(r)
        new_matrix.append(sub)
    return new_matrix
