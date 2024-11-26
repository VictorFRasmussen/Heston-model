import numpy as np
import fixed_income_derivatives_E2024 as fid
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.stats import norm

r0, a, b, sigma = 0.032, 1.2, 0.048, 0.1
T_max = 10
alpha = 0.5
M = int(T_max/3)