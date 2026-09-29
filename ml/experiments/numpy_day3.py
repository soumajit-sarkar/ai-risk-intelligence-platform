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

print()
risk_features = np.array([
    [0.6, 0.5, 0.8],
    [2.5, 1.4, 0.3],
    [7.5, 0.4, 0.4]
])

customer_multipliers = np.array([1.0, 1.5, 2.0])

adjusted_features = (
    risk_features * customer_multipliers.reshape(-1,1)
)

print("Adjusted risk features:")
print(adjusted_features)
print()

risk_score = amounts / 100
print("Vectorized risk score:")
print(risk_score)
print()

high_amount_flag = amounts >= 300
print("High amount flags:")
print(high_amount_flag)
print()


high_amount_numeric = np.where(high_amount_flag,1,0)
print("High amount numeric feature:")
print(high_amount_numeric)
print()

high_amount_flag_new_logic = amounts >= 500
print("High amount flags according to new logic: ")
print(high_amount_flag_new_logic)
print()

high_amount_numeric_new_logic = np.where(high_amount_flag_new_logic,1,0)
print("High amount numeric feature: according to new logic: ")
print(high_amount_numeric_new_logic)
print()

risk_flag = (amounts < 200) | (amounts >= 500)
print("Combined risk flag:")
print(risk_flag)
print()

risk_numeric = np.where(risk_flag,1,0)
print("Vectorized risk numeric:")
print(risk_numeric)

print()
normalized_amounts = (amounts - amounts.min()) / (amounts.max() - amounts.min())
print("Vectorized normalized amounts:")
print(normalized_amounts)
print()

amounts_with_nan = np.array([120, 250, np.nan, 800, 1500])
print(np.nanmean(amounts_with_nan))
print()

nan_mask = np.isnan(amounts_with_nan)
print("NaN mask:")
print(nan_mask)
print()

missing_values = amounts_with_nan[nan_mask]
print("Missing values:")
print(missing_values)
print()

normal_std = np.std(amounts)
nan_aware_std = np.nanstd(amounts_with_nan)
print("Normal standard deviation:")
print(normal_std)
print("NaN-aware standard deviation:")
print(nan_aware_std)
print()

nan_min = np.nanmin(amounts_with_nan)
nan_max = np.nanmax(amounts_with_nan)

print("NaN-aware minimum:")
print(nan_min)

print("NaN-aware maximum:")
print(nan_max)
print()


feature_amounts = np.array([120, 250, 800, 1500])
print("Feature amounts:")
print(feature_amounts)
print()

amount_feature = feature_amounts.reshape(-1,1)
print("Feature #1 - Amount:")
print(amount_feature)

print("Feature #1 shape:")
print(amount_feature.shape)
print()

normalized_amount_feature = (
    feature_amounts - feature_amounts.min()
) / (
    feature_amounts.max() - feature_amounts.min()
)

print("Feature #2 - Normalized Amount:")
normalized_amount_feature = normalized_amount_feature.reshape(-1, 1)
print(normalized_amount_feature)
print("Feature #2 shape:")
print(normalized_amount_feature.shape)

print()
high_risk_feature = (
    (feature_amounts < 200) |
    (feature_amounts >= 500)
)

print("Feature #3 - High Risk Flag:")
print(high_risk_feature)
print("Feature #3 shape:")
print(high_risk_feature.shape)
print()

high_risk_numeric_feature = np.where(
    high_risk_feature,
    1,
    0
)

print("Feature #3 - Numeric High Risk:")
high_risk_numeric_feature = high_risk_numeric_feature.reshape(-1, 1)
print(high_risk_numeric_feature)
print("Feature #3 numeric shape:")
print(high_risk_numeric_feature.shape)
print()

feature_matrix = np.column_stack((
       amount_feature,
       normalized_amount_feature,
       high_risk_numeric_feature 
 ))

print("Final feature matrix:")
print(feature_matrix)

print("Final feature matrix shape:")
print(feature_matrix.shape)