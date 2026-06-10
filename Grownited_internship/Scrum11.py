import numpy as np

np.random.seed(0)

arr = np.random.randint(1, 101, 50)

print("Array:")
print(arr)

sorted_arr = np.sort(arr)

print("\nSmallest 3 values:")
print(sorted_arr[:3])

print("\nLargest 3 values:")
print(sorted_arr[-3:])