import numpy as np

m1 = np.array([[1, 2], [3, 5]])
m2 = np.array([1, 2])

print(np.linalg.solve(m1, m2))
