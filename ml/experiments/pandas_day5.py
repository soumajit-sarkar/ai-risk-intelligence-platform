
import pandas as pd

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

print("Clean transaction dataset:")
print(transaction_df)
