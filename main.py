# generate related variables
from numpy import mean
from numpy import std
from matplotlib import pyplot
from variabled import *

# seed random number generator
# seed(1)
# prepare data
# data1 = 20 * randn(1000) + 100
# data2 = data1 + (10 * randn(1000) + 50)
# summarize

# print('length of trust1 is: %.3f' % len(trust1))
# print('length of var1 is: %.3f' % len(var1))


# print('trust: mean=%.3f stdv=%.3f' % (mean(trust1), std(trust1)))
# print('var1: mean=%.3f stdv=%.3f' % (mean(var1), std(var1)))
# plot
# pyplot.scatter(trust1, var1)
# pyplot.show()

# calculate the covariance between two variables
from numpy import cov

covariance = cov(trust1, var1)
print(covariance)

# calculate the Pearson's correlation between two variables
from scipy.stats import pearsonr

corr, _ = pearsonr(trust1, var1)
print('Pearsons correlation between V1 and trust: %.3f' % corr)

# calculate the spearmans's correlation between two variables

from scipy.stats import spearmanr

corr, _ = spearmanr(trust1, var1)
print('Spearmans correlation between V1 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var2)
print('Pearsons correlation between V2 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var2)
print('Spearmans correlation between V2 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var3)
print('Pearsons correlation between V3 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var3)
print('Spearmans correlation between V3 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var4)
print('Pearsons correlation between V4 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var4)
print('Spearmans correlation between V4 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var5)
print('Pearsons correlation between V5 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var5)
print('Spearmans correlation between V5 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var6)
print('Pearsons correlation between V6 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var6)
print('Spearmans correlation between V6 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, var8)
print('Pearsons correlation between V8 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, var8)
print('Spearmans correlation between V8 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, literacyscore1)
print('Pearsons correlation between literacyscore1 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, literacyscore1)
print('Spearmans correlation between literacyscore1 and trust: %.3f' % corr)

corr, _ = pearsonr(trust1, literacyscore2)
print('Pearsons correlation between literacyscore2 and trust: %.3f' % corr)
corr, _ = spearmanr(trust1, literacyscore2)
print('Spearmans correlation between literacyscore2 and trust: %.3f' % corr)