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

print()

print("Transaction amounts:")

amounts = transactions[:, 0]

print(amounts)

print()

print("Transaction amounts increased by 10%:")

print(amounts * 1.10)

print()

amounts = transactions[:,0]
average_amounts = transactions[:,2]
difference = amounts - average_amounts
print(difference)

print()
print("Relative transaction amount compared with average amount:")
relative_amount = amounts / average_amounts
print(relative_amount)


print()

print("Relative deviation from average amount:")

relative_deviation = (amounts - average_amounts) / average_amounts

print(relative_deviation)

print()

print("Average transaction amount:")

average_transaction_amount  = np.mean(amounts)

print(average_transaction_amount)

print()
print("Deviation from overall average:")
deviation_from_average  = amounts - average_transaction_amount
print(deviation_from_average)

print()

print("Amounts used for standard deviation:")
print(amounts)

print()

print("Mean used for standard deviation:")
print(np.mean(amounts))

print()
print("Standard deviation of transaction amounts:")
standard_deviation = np.std(amounts)
print(standard_deviation)

print()
print("Minimum Transaction amount: ")
minimum_amount = np.min(amounts)
print(minimum_amount)

print()

print("Maximum transaction amount: ")
maximum_amount = np.max(amounts)
print(maximum_amount)

print()
print("Sum of transaction amounts: ")
total_amount = np.sum(amounts)
print(total_amount)

print()
median_amount = np.median(amounts)
print("Median transaction amount: ")
print(median_amount)

print()
print("50th percentile of transaction amounts:")
print(np.percentile(amounts, 50))
print()

print()

print("25th percentile of transaction amounts:")
shorted_amount = np.short(amounts)
print(shorted_amount)
print(np.percentile(shorted_amount, 25))
print()

