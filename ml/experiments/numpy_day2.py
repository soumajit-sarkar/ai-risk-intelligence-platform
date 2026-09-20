import numpy as np

amounts = np.array([120.00,250.00,800.00])
q1 = np.percentile(amounts,25)
q2 = np.percentile(amounts,50)
q3 = np.percentile(amounts,75)

iqr = q3 - q1

print("Transaction amount: ")
print(amounts)
print()

print("Q1: ")
print(q1)
print()

print("Q2: ")
print(q2)
print()

print("Q3: ")
print(q3)
print()

print("IQR: ")
print(iqr)
print()

print("Lower Outlier Bound: ")
lower_bound= q1 - (1.5 * iqr)
print(lower_bound)
print()

print("Upper Outlier Bound: ")
upper_bound= q3 + (1.5 * iqr)
print(upper_bound)
print()

outlier_mask = (amounts < lower_bound) | (amounts > upper_bound)
print(outlier_mask)