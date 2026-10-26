import torch

transaction_amount = torch.tensor(500.0)

transaction_amounts = torch.tensor([500.0, 800.0, 300.0])

print("Single amount:", transaction_amount)
print("Single amount shape:", transaction_amount.shape)
print("Single amount dimensions:", transaction_amount.ndim)
print("Single amount data type:", transaction_amount.dtype)

print()

print("Multiple amounts:", transaction_amounts)
print("Multiple amounts shape:", transaction_amounts.shape)
print("Multiple amounts dimensions:", transaction_amounts.ndim)
print("Multiple amounts data type:", transaction_amounts.dtype)

print()

amounts = torch.tensor([500.0, 800.0, 300.0, 1200.0])
print("\nFour transaction amounts:", amounts)
print("Shape: ",amounts.shape)
print("Dimensions: ", amounts.ndim)
print("Data type: ", amounts.dtype)

print()

transaction_features = torch.tensor([
    [500.0, 120.0, 0.0],
    [800.0, 45.0, 1.0],
    [300.0, 365.0, 0.0],
    [1200.0, 12.0, 3.0],
])

print("\nTransaction features:")
print(transaction_features)

print("Shape:", transaction_features.shape)
print("Dimensions:", transaction_features.ndim)

print()

too2 = transaction_features[1]

print("\n TOO2 features: ", too2)
t002_account_age = transaction_features[1,1]
print("T002 account age:", t002_account_age)