import random
import numpy as np
import matplotlib.pyplot as plt
import time


####### measuring time pt1

start_time = time.clock()
end_time = time.clock()

end_time - start_time

####### practice of plotting pt1

x = np.linspace(0, 10, 20)
y1 = x**2
y2 = x**1.5

plt.plot([0, 1, 2], [0, 1, 4], "rd-", label="Hidden o.o")
plt.plot(x, y1, "go-", label="Firsto")
plt.plot(x, y2, "gs-", linewidth=2, markersize=6, label="Seccundo")
plt.xlabel("$X$")  # LaTeX styled
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 55])  # xmin, xmax, ymin, ymax
plt.legend(loc="upper left")
# plt.savefig("aplot.pdf")

####### practice of plotting pt2

x = np.logspace(-1, 1, 40)
y1 = x**2
y2 = x**1.5

plt.plot([0, 1, 2], [0, 1, 4], "rd-", label="Hidden o.o")
plt.loglog(x, y1, "go-", label="Firsto")
plt.loglog(x, y2, "gs-", linewidth=2, markersize=6, label="Seccundo")
plt.xlabel("$X$")  # LaTeX styled
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 55])  # xmin, xmax, ymin, ymax
plt.legend(loc="upper left")
# plt.savefig("bplot.pdf")

####### *elevator music*

x = np.random.normal(size=1000)
plt.hist(x, normed=True, bins=np.linspace(-5, 5, 201))

####### practice of plotting pt3

x = np.random.gamma(2, 3, size=100000)

plt.figure()
plt.subplot(221)
plt.hist(x, bins=30)
plt.subplot(222)
plt.hist(x, bins=30, normed=True)
plt.subplot(223)
plt.hist(x, bins=30, cumulative=30)
plt.subplot(224)
plt.hist(x, bins=30, normed=True, cumulative=30, histtype="step")
# plt.savefig("ahist.pdf")

####### practice of plotting pt4

rolls = []
for k in range(100000):
    rolls.append(random.choice([1, 2, 3, 4, 5, 6]))
plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))

####### measuring time pt2

start_time = time.clock()

ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1, 2, 3, 4, 5, 6])
        y = y + x
    ys.append(y)

end_time = time.clock()
print(end_time - start_time)

plt.hist(ys)

####### practice of random random random

np.random.random()  # random number between 0 and 1
np.random.random(5)  # 5 arrays of ^
np.random.random((5, 3))  # array with 5 rows and 3 columns of ^^

np.random.normal(0, 1)  # a number from the normal distribution (here standard.. since mean = 0, standard deviation = 1)
np.random.normal(0, 1, 5)  # an array of 5 ^
np.random.normal(0, 1, (2, 5))  # a 2D array with two rows and 5 columns

####### measuring time pt3

start_time = time.clock()

X = np.random.randint(1, 7, (1000000, 10))  # a 1000000 x 10 array with random ints from 1-6
Y = np.sum(X, axis=1)

end_time = time.clock()
print(end_time - start_time)

plt.hist(Y)

# woobwoob explanations
np.sum(X)  # sums all of the data
np.sum(X, axis=0)  # sums all the rows
np.sum(X, axis=1)  # sums all the columns

####### random walk simulation

X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0, 1, (2, 10000))
X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis=1)
plt.plot(X[0], X[1], "go-")
# plt.savefig("randomwalk.pdf")
