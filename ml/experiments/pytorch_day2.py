import pandas as pd
import torch
from sklearn.model_selection import train_test_split

transactions = pd.DataFrame({
    "amount": [500.0, 800.0, 300.0, 1200.0],
    "account_age_days": [120.0, 45.0, 365.0, 12.0],
    "failed_attempts": [0.0, 1.0, 0.0, 3.0],
    "historical_outcome": [
        "low_risk",
        "high_risk",
        "low_risk",
        "high_risk",
    ],
})

print("Transaction data:")
print(transactions)

print("\nDataFrame shape:", transactions.shape)
print("DataFrame data types:")
print(transactions.dtypes)

print()

transaction_array = transactions.to_numpy()
print("\nNumPy array:")
print(transaction_array)
print()

print("NumPy array shape: ",transaction_array.shape)
print("NumPy array data type: ",transaction_array.dtype)

print()

# Separate input features (X) from target labels (y)
X = transactions[
    ["amount", "account_age_days", "failed_attempts"]
]

y = transactions["historical_outcome"]

print("\nInput features (X):")
print(X)

print("\nTarget labels (y):")
print(y)

print("\nX shape:", X.shape)
print("y shape:", y.shape)

print()

y_encoded = y.map(
    {
        "low_risk" : 0,
        "high_risk" : 1
    }
)
print("\nEncoded target labels:")
print(y_encoded)

print("\nEncoded labels data type:", y_encoded.dtype)
print("Are all labels encoded?", y_encoded.notna().all())

print()

# Convert input features into a PyTorch tensor
X_tensor = torch.tensor(
    X.to_numpy(),
    dtype=torch.float32,
)

print("\nInput feature tensor (X_tensor):")
print(X_tensor)

print("X_tensor shape:", X_tensor.shape)
print("X_tensor dtype:", X_tensor.dtype)

print()

y_tensor = torch.tensor(
    y_encoded.to_numpy(),
    dtype=torch.long
)
print("\nTarget tensor (y_tensor):")
print(y_tensor)

print("y_tensor shape:", y_tensor.shape)
print("y_tensor dtype:", y_tensor.dtype)

print("\nDo X and y have the same number of samples?")
print(X_tensor.shape[0] == y_tensor.shape[0])

print()

X_train,X_test,y_train,y_test = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.25,
    random_state=42
)

print("\nTraining and testing split:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)