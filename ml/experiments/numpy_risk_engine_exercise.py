import numpy as np

amounts = np.array([150, 300, 450, 800, 1200, 2000])
print("Transaction amounts:")
print(amounts)
print()

normalized_amounts = (amounts - amounts.min()) / (amounts.max() - amounts.min())
print("The normalized values are: ")
print(normalized_amounts)
print()

high_risk_flag = (amounts < 200) | (amounts >= 1000)
print("High risk flag boolean are: ")
print(high_risk_flag)
print()

high_risk_flag_value = amounts[high_risk_flag]
print("High risk flag values are: ")
print(high_risk_flag_value)

high_risk_numeric = np.where(high_risk_flag,1,0)
print("High risk numeric values are: ")
print(high_risk_numeric)

amount_shape = amounts.reshape(6,-1)
print("reshaping the amounts 1d array: ")
print(amount_shape)
print("Shpae of the amount: ")
print(amount_shape.shape)
print()

normalized_amounts_reshape = normalized_amounts.reshape(6,-1)
print("reshaping the normalized amounts 1d array: ")
print(normalized_amounts_reshape)
print("Shpae of the normalized amount")
print(normalized_amounts_reshape.shape)
print()


high_risk_numeric_reshape = high_risk_numeric.reshape(6,-1)
print("reshaping the high risk numeric amounts 1d array: ")
print(high_risk_numeric_reshape)
print("Shpae of the high risk numeric amount")
print(high_risk_numeric_reshape.shape)
print()

feature_matrix = np.column_stack((
    amount_shape,
    normalized_amounts_reshape,
    high_risk_numeric_reshape
))

print("Final feature matrix:")
print(feature_matrix)

print("Final feature matrix shape:")
print(feature_matrix.shape)


