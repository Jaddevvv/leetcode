# https://www.deep-ml.com/problem/Gini%20Impurity

# TRYING NOT TO USE NUMPY 
# import numpy as np


def gini_impurity(y):
    distinct_values = []
    sum_pvalues = 0

    for item in y:
        if item not in distinct_values:
            distinct_values.append(item)

    for value in distinct_values:
        value = y.count(value)/len(y)
        sum_pvalues += value ** 2
    
    result = 1 - sum_pvalues
    return round(result,3)

print(gini_impurity([0, 1, 1, 1, 0]))