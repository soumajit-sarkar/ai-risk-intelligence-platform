import numpy as np

amounts = [100,200,300,400]

numpy_amounts = np.array(amounts)

print("Python list: ")
print(amounts)

print()

print("Numpy array: ")
print(numpy_amounts)

print()

print("Numpy array * 1.10")
print(numpy_amounts * 1.10)

print()

print("Type of Python list:")
print(type(amounts))

print()

print("Type of NumPy array:")
print(type(numpy_amounts))

print()
print("Number of dimensions:")
print(numpy_amounts.ndim)

print()
print("Shape: ")
print(numpy_amounts.shape)

print()
print("Number of elements: ")
print(numpy_amounts.size)

print()
print("Data type: ")
print(numpy_amounts.dtype)

print()
decimal_amounts = np.array([100.50, 200.75, 300.25, 400.00])

print()
print("Decimal NumPy array:")
print(decimal_amounts)

print()
print("Decimal array dtype:")
print(decimal_amounts.dtype)

print()
mixed_amounts = np.array([100, 200.50, 300, 400])

print()
print("Mixed NumPy array:")
print(mixed_amounts)

print()
print("Mixed array dtype:")
print(mixed_amounts.dtype)

print()
transactions = np.array([
    [250.00, 3, 125.50],
    [800.00, 8, 400.25],
    [120.00, 1, 80.00],
])

print()
print("Transaction feature matrix:")
print(transactions)

print()
print("Number of dimensions:")
print(transactions.ndim)

print()
print("Shape:")
print(transactions.shape)

print()
print("Number of elements:")
print(transactions.size)

print()
print("Data type:")
print(transactions.dtype)


print()
print("Transaction 1 amount:")
print(transactions[0, 0])

print()
print("Transaction 2 amount:")
print(transactions[1, 0])

print()
print("Transaction 3 velocity:")
print(transactions[2, 1])


print()
print("Transaction 1:")
print(transactions[0])

print()
print("Transaction 2:")
print(transactions[1])

print()
print("Transaction 1:")
print(transactions[:,0])

print()
print("Transaction 2:")
print(transactions[:,1])

print()
print("All average transaction amounts:")
print(transactions[:, 2])

print()
print("First two transactions:")
print(transactions[0:2])

print()
print("First two transactions - amount and velocity:")
print(transactions[0:2,0:2])

print(transactions[0])