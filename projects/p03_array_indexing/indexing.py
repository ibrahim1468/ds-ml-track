import numpy as np

arr = np.arange(30).reshape(6, 5)

print(arr)
print("3rd Row: ", arr[2])
print("Last Columns: ", arr[:, -1])
print("2x2 block from the center: ", arr[2:4, 1:3])
print("Every other row: ", arr[::2])

arr1 = np.arange(5).reshape(5, )
arr2 = np.arange(6).reshape(6, )

arr1_bc = arr + arr1
print(arr1_bc)

arr3 = np.arange(6).reshape(6, 1)
arr3_bc = arr + arr3
print(arr3_bc)
#Broadcasting works by aligning shapes from the right and allowing operations only when each dimension pair is equal or one of them is 1, otherwise it fails.