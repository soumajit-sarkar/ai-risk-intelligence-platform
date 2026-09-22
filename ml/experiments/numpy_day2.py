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


print()
print("High risk flag:")
high_risk_flag = outlier_mask | high_amount_flag
print(high_risk_flag)

print()
print("High risk transactions:")
print(amounts[high_risk_flag])

print()
high_risk_count  = np.sum(high_risk_flag)
print("High risk flag count:")
print(high_risk_count)
total_transactions = high_risk_flag.size
print("Total transactions are: ")
print(total_transactions)
high_risk_rate = (high_risk_count / total_transactions) * 100
print("High risk rate: ")
print(high_risk_rate)

print()
print("High risk numeric feature:")
high_risk_numeric = np.where(high_risk_flag,1,0)
print(high_risk_numeric)


print()
print("Capped transaction amount:")
capped_amounts = np.clip(amounts, 100, 1000)
print(capped_amounts)


print()
print("Min-Max normalized amount:")

min_amount = np.min(amounts)
max_amount = np.max(amounts)

normalized_amounts = (amounts - min_amount) / (max_amount - min_amount)

print(normalized_amounts)