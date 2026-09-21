import numpy as np

amounts = np.array([120.00,250.00,800.00,1500.00])
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
print("Outlier status:")
print(outlier_mask)

print()
print("Transactions greater than 500:")
print(amounts[amounts > 500])

print()
print("High amount flag:")
high_amount_flag = amounts > 1000
print(high_amount_flag)

print()
print("High amount transactions:")
print(amounts[high_amount_flag])


print()
print("Medium-high amount flag:")
medium_high_flag = (amounts > 500) & (amounts <= 1000)
print(medium_high_flag)

print()
print("Medium-high amount transactions:")
print(amounts[medium_high_flag])

print()
print("Risk flag:")
risk_flag = (amounts < 200) | (amounts > 1000)
print(risk_flag)

print()
print("Risk transactions:")
print(amounts[risk_flag])