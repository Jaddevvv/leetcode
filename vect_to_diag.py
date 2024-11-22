# https://www.deep-ml.com/problem/Convert%20Vector%20to%20Diagonal%20Matrix

def make_diagonal(x):
    nbline = len(x)
    empty_diag = [[0] * nbline for _ in range(nbline)]

    iteration = 0
    while iteration < nbline:
        empty_diag[iteration][iteration] = x[iteration]
        iteration += 1

    return empty_diag