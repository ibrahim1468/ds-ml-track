import numpy as np
import time
import random as r
import matplotlib.pyplot as plt

N = [100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]

speeds = []
ptimes = []
ntimes = []

for n in N:
    list1 = [r.random() for _ in range(n)]
    list2 = [r.random() for _ in range(n)]

    arr1 = np.random.rand(n)
    arr2 = np.random.rand(n)

    # Python timing
    start_python = time.perf_counter()
    list_addition = []
    for i in range(n):
        list_addition.append(list1[i] + list2[i])
    end_python = time.perf_counter()
    time_python = end_python - start_python

    # NumPy timing
    start_numpy = time.perf_counter()
    arr_addition = arr1 + arr2
    end_numpy = time.perf_counter()
    time_numpy = end_numpy - start_numpy

    speedup = time_python / time_numpy if time_numpy > 0 else float("inf")

    speeds.append(speedup)
    ptimes.append(time_python)
    ntimes.append(time_numpy)

plt.plot(N, speeds, marker="o", c="r")
plt.xscale("log")
plt.title("Speedup vs N (log scale)")
plt.xlabel("N")
plt.ylabel("Speedup (Python / NumPy)")
plt.grid(True)
plt.show()

plt.plot(N, ptimes, marker="o", label="Python")
plt.plot(N, ntimes, marker="o", label="NumPy")

plt.xscale("log")
plt.yscale("log")

plt.title("Execution Time vs N (log-log)")
plt.xlabel("N")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True, which="both")
plt.show()