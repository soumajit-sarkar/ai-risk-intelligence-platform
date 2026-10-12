
import pandas as pd

# Transaction dataset
transaction_data = {
    "transaction_id": ["T101", "T102", "T103", "T104", "T105", "T106"],
    "customer_id": ["C001", "C001", "C002", "C001", "C002", "C003"],
    "amount": [500, 2500, 800, 12000, 1500, 400],
    "country": ["IN", "IN", "US", "IN", "US", "IN"],
    "channel": ["WEB", "WEB", "MOBILE", "ATM", "MOBILE", "WEB"],
}

transaction_df = pd.DataFrame(transaction_data)

# Customer dataset
customer_data = {
    "customer_id": ["C001", "C002", "C003"],
    "customer_segment": ["PREMIUM", "STANDARD", "NEW"],
    "account_age_days": [1200, 400, 30],
}

customer_df = pd.DataFrame(customer_data)

print("TRANSACTIONS")
print(transaction_df)

print("\nCUSTOMERS")
print(customer_df)
print()

"""
Keep all six transactions and attach the matching customer segment and account age using customer_id.
"""

enriched_transactions = pd.merge(
    transaction_df,
    customer_df,
    on="customer_id",
    how="left"
)

print("\nENRICHED TRANSACTIONS")
print(enriched_transactions)