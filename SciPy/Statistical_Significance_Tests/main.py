import numpy as np

# T-Test
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)
print(res.pvalue)

# KS-Test
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)
print(res.pvalue)

# Statistical Description of Data
from scipy.stats import describe

v = np.random.normal(size=100)

res = describe(v)

print(res)

# Normality Test
from scipy.stats import skew, kurtosis, normaltest

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))
print(normaltest(v))