
import pandas as pd
import numpy as np
# --------------------------------------------------
# 1. Build the transaction dataset
# --------------------------------------------------

transaction_ids = ["T101", "T102", "T103", "T104", "T105", "T106"]
customer_ids = ["C001", "C001", "C002", "C001", "C002", "C003"]
amounts = [500, 2500, 800, 12000, 1500, 400]
countries = ["IN", "IN", "US", "IN", "US", "IN"]
channels = ["WEB", "WEB", "MOBILE", "ATM", "MOBILE", "WEB"]

transactions = {
    "customer_id": customer_ids,
    "amount": amounts,
    "country": countries,
    "channel": channels,
}

transaction_df = pd.DataFrame(
    transactions,
    index=transaction_ids,
)

# --------------------------------------------------
# 2. Chapter 9 — Sorting, Ranking and Transformation
# --------------------------------------------------

print("Original transaction dataset:")
print(transaction_df)
print()


print("Transactions ordered by amount (highest to lowest):")
ordered_transactions = transaction_df.sort_values(
    by="amount",
    ascending=False
)

print(ordered_transactions)
print()

transaction_df["amount_rank"] = transaction_df["amount"].rank(
    ascending=False,
    method="min",
)

print(transaction_df)
print()

"""
New business requirement: The risk team wants to label every transaction as "HIGH" when its amount is above ₹5,000, and "NORMAL" otherwise.
"""

previous_transaction_amount = transaction_df["amount"].shift()
amount_change = transaction_df["amount"] - previous_transaction_amount
transaction_df["amount_change"] = amount_change
# print(transaction_df)
greater_than_5000 = transaction_df["amount_change"] > 5000
transaction_df["amount_category"] = np.where(
    greater_than_5000,
    "HIGH",
    "NORMAL",
)

print(transaction_df)