import pandas as pd

transaction_ids = ["T001", "T002", "T003", "T004", "T005", "T006", "T007"]

customer_id = ["C001", "C002", "C001", "C003", "C001", "C002", "C004"]

amounts = [500, 1200, None, 2500, 800, None, 1500]

country = ["IN", "US", "US", "UK", "IN", None, "IN"]

channel = ["WEB", "ATM", "MOBILE", "WEB", "MOBILE", "WEB", None]

transactions = {
    "customer_id": customer_id,
    "amount": amounts,
    "country": country,
    "channel": channel
}

transaction_df = pd.DataFrame(
    transactions,
    index=transaction_ids
)

print("Transaction DataFrame:")
print(transaction_df)
print()

"""
Business requirement
Before performing any risk calculations, determine which columns contain missing transaction data and how many missing values each column has."
"""
get_missing_values = transaction_df.isnull()
get_missing_values_and_count = get_missing_values.sum()
print(get_missing_values)
print()
print(get_missing_values_and_count)
print()

"""
Business requirement
The Risk Engine should identify every transaction that has at least one missing field.

axis=0 = columns
axis=1 = rows
"""
get_rows_with_nan = get_missing_values.any(axis=1)
print(get_rows_with_nan)
print()
print(transaction_df.loc[get_rows_with_nan])
print()

"""
Handle missing amount values — decide what should happen before risk calculations
"""
print(transaction_df.loc[~transaction_df["amount"].isnull()])
print()
"""
Final Risk Data-Quality Decision
"""

risk_ready_df = pd.DataFrame(transaction_df.loc[~transaction_df["amount"].isnull()])
print("Risk ready dataframe: ")
print(risk_ready_df)
