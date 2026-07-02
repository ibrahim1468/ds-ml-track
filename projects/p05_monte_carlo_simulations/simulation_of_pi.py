import numpy as np
N = [100, 1000, 100_000, 10_000_000]

for n in N:
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)

    total_points = x**2 + y**2
    circle_array = total_points[total_points <= 1]
    pi = 4 * ((circle_array.size)/(total_points.size))
    abs_error = abs(pi - np.pi)
    
    print(f"Value of π for {n:,}: {pi:.6f} "
          f"with absolute error {abs_error:.6f}")