from tools import *
from scipy.stats import chi2
import numpy as np
import struct
import matplotlib.pyplot as plt
import math
from collections import defaultdict


class Distribution(object):
    def __init__(self, teta):
        self.teta = teta

    def dis(self, x):
        return 1 - math.exp(-self.teta * x)  #

    def probability(self, bounds):
        print(bounds)
        p = self.dis(bounds[1]) - self.dis(bounds[0])
        print(p)
        return p


def estimate(vectors):
    return 1 / (mean(vectors))


def xCriteria(counted, length, dis):
    sum = 0
    for i in counted.keys():
        sum += float((counted[i] - dis.probability(i) * length) ** 2) / (
                dis.probability(i) * length)

    return sum


def prob(bounds):
    pass


def rygalin(seq, dis):
    max_value = max(seq)
    n = 1 + math.floor(3.322 * math.log10(len(seq)))
    N = len(seq)
    bounds = dict()
    nu = n - 1
    for i in range(nu):
        bounds[i] = ((max_value / nu) * i, (max_value / nu) * (i + 1))
    bounds[nu] = (max_value, math.inf)
    count_intervals = defaultdict(lambda: 0)
    for i in seq:
        for j in range(n):
            if bounds[j][0] <= i < bounds[j][1]:
                count_intervals[j] += 1
                break
    print(count_intervals)
    xi = sum([pow((i - dis.probability(bounds[k]) * N), 2) / (
            dis.probability(bounds[k]) * N) for k, i in
              count_intervals.items()])
    return xi


b = 4

vectors = vectorsFromFile("3.data", b)

teta = estimate(vectors)
print("teta: ", teta)
dis = Distribution(teta)
max_value = max(vectors)
criteria = rygalin(vectors, dis)
df = 1 + math.floor(3.322 * math.log10(len(vectors))) - 1
print('Degrees of freedom: ', df)
print('Criteria X^2: ', criteria)

percent = 0.05
print("Alpha = %d" % (1 - percent))
quantile = chi2.ppf(1 - percent, df)

print('Quantile is ', quantile)

if (criteria < quantile):
    print('Hypothesis is right!')
else:
    print('Hypothesis is wrong!')

x = np.sort(vectors)
y = np.arange(len(x)) / float(len(x))
plt.plot(x, y)
plt.savefig("graph.png")
plt.close()
