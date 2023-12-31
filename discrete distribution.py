import numpy as np

L = [int(i) for i in input().split()]
N = len(L)
print(N)
M = max(L)
print(M)

x = []
frequency_of_x = []

for i in range(M + 1):
    c = 0
    for j in range(N):
        if L[j] == i:
            c += 1
    frequency_of_x.append(c)
    x.append(i)

print(x)
print(frequency_of_x)

sum_of_frequency = np.sum(frequency_of_x)
print(sum_of_frequency)

prob_of_x = []

for i in range(M + 1):
    prob_of_x.append(frequency_of_x[i] / sum_of_frequency)

mean = np.inner(x, prob_of_x)
print(mean)

EX2 = np.inner(np.square(x), prob_of_x)
variance = EX2 - mean ** 2
print(variance)

standard_deviation = np.sqrt(variance)
print(standard_deviation)

print("The Mean arrival rate is %.3f" % mean)
print("The Variance of arrival from feeder is %.3f" % variance)
print("The Standard deviation of arrival from feeder is %.3f" % standard_deviation)
