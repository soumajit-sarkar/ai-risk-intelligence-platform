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

print("Column data types:")
print(transaction_df.dtypes)

print()
get_in_valid_amount = transaction_df["amount"] < 0
print(get_in_valid_amount)

invalid_test_df = pd.DataFrame(
    {
        "customer_id": ["C005"],
        "amount": [-500],
        "country": ["IN"],
        "channel": ["WEB"]
    },
    index=["T008"]
)

print()
print("Invalid test transaction:")
print(invalid_test_df)

print()
get_invalid_amount = invalid_test_df["amount"] < 0
print(get_invalid_amount)
print()


invalid_amount_mask = (
    transaction_df["amount"].isnull()
    |
    (transaction_df["amount"] < 0)
)

print(invalid_amount_mask)


"""
Display only transactions that are invalid for monetary risk calculations.
"""
print(transaction_df.loc[invalid_amount_mask])