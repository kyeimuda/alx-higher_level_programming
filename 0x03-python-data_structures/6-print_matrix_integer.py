#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        length = len(index)
        for subindex in index:
            if subindex == index[-1]:
                print("{:d}".format(subindex), end="")
            else:
                print("{:d}".format(subindex), end=" ")
        print()
            
