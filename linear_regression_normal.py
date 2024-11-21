# https://www.deep-ml.com/problem/Linear%20Regression%20Using%20Normal%20Equation

import numpy as np
from numpy.linalg import inv

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	theta = inv(np.transpose(X)@(X))@np.transpose(X)@y
	return theta