import numpy as np

# Creating a 2D array
original_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original array:\n{original_array}")

# Flattening the array using ravel() with default C-order
flattened_array = np.ravel(original_array)
print(f"Flattened array (C-order): {flattened_array}")

# Example of F-order (column by column)
flattened_array_f = np.ravel(original_array, order='F')
print(f"Flattened array (F-order): {flattened_array_f}")

# Demonstrating that modifying the flattened array can affect the original
flattened_array[0] = 99
print(f"Modified original array: \n{original_array}")