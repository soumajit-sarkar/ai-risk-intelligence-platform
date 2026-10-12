
import pandas as pd

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
# 2. Create risk-engine features
# --------------------------------------------------

# Feature 1: Transaction amount exceeds ₹5,000
transaction_df["high_amount_flag"] = (
    transaction_df["amount"] > 5000
)

# Feature 2: Transaction was performed through an ATM
transaction_df["is_atm_transaction"] = (
    transaction_df["channel"] == "ATM"
)

# Feature 3: Both conditions are true
transaction_df["high_amount_atm_flag"] = (
    transaction_df["high_amount_flag"]
    & transaction_df["is_atm_transaction"]
)

# Feature 4: Average amount for each customer's transactions
customer_average = (
    transaction_df.groupby("customer_id")["amount"]
    .transform("mean")
)

transaction_df["customer_average"] = customer_average

# Feature 5: Transaction amount exceeds its customer's average
transaction_df["above_customer_average_flag"] = (
    transaction_df["amount"]
    > transaction_df["customer_average"]
)

# --------------------------------------------------
# 3. Display the final dataset
# --------------------------------------------------

print("Final transaction dataset with engineered features:")
print(transaction_df)
print()

print("Transactions above their customer's average:")
print(
    transaction_df.loc[
        transaction_df["above_customer_average_flag"]
    ]
)
