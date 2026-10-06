import pandas as pd

transaction_ids = ["T001", "T002", "T003", "T004", "T005", "T006"]
customer_id = ["C001", "C002", "C001", "C003", "C001", "C002"]
amounts = [500, 1200, 300, 2500, 800, 700]
country = ["IN", "US", "IN", "UK", "IN", "US"]
channel = ["WEB", "ATM", "MOBILE", "WEB", "MOBILE", "WEB"]

transaction_amounts = pd.Series(
    amounts,
    index=transaction_ids
)

print("Transaction Amounts:")
print(transaction_amounts)

print()
print("Amount for T004:")
print(transaction_amounts.loc["T004"])

print()
print("Amount at position 4:")
print(transaction_amounts.iloc[4])

print()
transactions = {
    # "transaction_id":transaction_ids,
    "customer_id": customer_id,
    "amount":amounts,
    "country":country,
    "channel":channel
}
transaction_df = pd.DataFrame(transactions,index=transaction_ids)

print("Transaction DataFrame:")
print(transaction_df)
print()
print(transaction_df.loc[:,("customer_id","amount")])
print()
print(transaction_df.loc[:,"amount"] > 1000)
print()
print(transaction_df.loc[transaction_df.loc[:,"amount"] > 1000,:])
print()
print(transaction_df.loc[transaction_df.loc[:,'country'] == "IN",:])
print()
print(transaction_df.loc[(transaction_df.loc[:,"country"] == "IN") & (transaction_df.loc[:,"amount"] > 500),:])