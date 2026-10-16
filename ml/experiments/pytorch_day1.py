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