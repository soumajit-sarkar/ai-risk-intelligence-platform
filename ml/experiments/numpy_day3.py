import numpy as np

amounts = np.array([120, 250, 800, 1500, 330])
total_amounts = np.sum(amounts)

print("Total transaction amount:")
print(total_amounts)

print()
transactions = np.array([
    [120, 250, 800],
    [500, 700, 300],
    [1500, 200, 400]
])

print("Transaction matrix:")
print(transactions)

print()
customer_totals = np.sum(transactions, axis=1)
customer_average = np.mean(transactions, axis=1)

print("Total per customer:")
print(customer_totals)
print("Average per customer:")
print(customer_average)
print()

res = np.std(transactions,axis=1)
print("Std Dev: ")
print(res)

print()
customer_min = np.min(transactions, axis=1)
customer_max = np.max(transactions, axis=1)

print("Minimum transaction per customer:")
print(customer_min)

print("Maximum transaction per customer:")
print(customer_max)

print()
transaction_range = customer_max - customer_min
print("Transaction range")
print(transaction_range)

print()
print("Transaction matrix shape:")
transactions_shape = transactions.shape
print(transactions_shape)
print()

print("transaction size: ")
transaction_size = transactions.size
print(transaction_size)
print()

flattened_transactions = transactions.reshape(transaction_size)
print("Reshaped transactions:")
print(flattened_transactions)
print()

print()
print("Reshaped shape:")
print(flattened_transactions.shape)
print()

row_vector = transactions.reshape(1, transactions.size)

print("Row vector:")
print(row_vector)
print("Row vector shape:")
print(row_vector.shape)

print()

column_vector = transactions.reshape(transactions.size, 1)
print("Column vector:")
print(column_vector)
print("Column vector shape:")
print(column_vector.shape)

print()
column_vector = transactions.reshape(transactions.size, 1)
print("Column vector:")
print(column_vector)
print("Column vector shape:")
print(column_vector.shape)
print()

print()
flattened = transactions.flatten()
raveled = transactions.ravel()
print("Original first value:")
print(transactions[0, 0])
print("Flattened first value:")
print(flattened[0])
print("Raveled first value:")
print(raveled[0])
print()


flattened[0] = 9999
raveled[1] = 8888
print("After modification:")
print("Original transactions:")
print(transactions)
print()
print("Flattened:")
print(flattened)
print()
print("Raveled:")
print(raveled)


