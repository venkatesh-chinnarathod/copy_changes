import numpy as np

# Create arrays
values = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(5)
ones = np.ones((2, 3))
sequence = np.arange(0, 10, 2)

# Array operations
print("Values:", values)
print("Mean:", np.mean(values))
print("Median:", np.median(values))
print("Sum:", np.sum(values))
print("Maximum:", np.max(values))
print("Minimum:", np.min(values))
print("Standard deviation:", np.std(values))
print("Squared values:", np.square(values))
print("Square root:", np.sqrt(values))
print("Zeros:", zeros)
print("Ones:", ones)
print("Sequence:", sequence)
