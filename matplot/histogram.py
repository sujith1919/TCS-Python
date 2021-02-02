import matplotlib.pyplot as plt
from numpy.random import normal
numbers = normal(size=1000)
plt.hist(numbers)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
#plt.show()
plt.savefig("h.png")