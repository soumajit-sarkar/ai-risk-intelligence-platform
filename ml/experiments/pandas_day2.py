import pandas as pd

transaction_ids = ["T001", "T002", "T003", "T004", "T005", "T006"]
customer_id = ["C001", "C002", "C001", "C003", "C001", "C002"]
amounts = [500, 1200, 300, 2500, 800, 700]
country = ["IN", "US", "US", "UK", "IN", "US"]
channel = ["WEB", "ATM", "MOBILE", "WEB", "MOBILE", "WEB"]

transactions = { 
    "customer_id":customer_id,
    "amount":amounts,
    "country":country,
    "channel":channel
}

transaction_df = pd.DataFrame(transactions,index=transaction_ids)

print("Transaction DataFrame:")
print(transaction_df)
print()

# print(transaction_df.groupby("customer_id")["amount"].sum())
# print()

# print(transaction_df.groupby("customer_id")["amount"].sum())
# print()

# print("Find the average transaction amount for each customer: ")
# print(transaction_df.groupby("customer_id")["amount"].mean())
# print()

# print("For each customer, determine how many transactions they have made: ")
# print(transaction_df.groupby("customer_id")["amount"].count())
# print()

# print("Count every transaction, including rows where amount is null: ")
# print(transaction_df.groupby("customer_id").size())
# print()

# print("How can we tell Pandas to perform multiple aggregations on this grouped data at the same time? ")
# print(transaction_df.groupby("customer_id")["amount"].agg(["sum","mean"]))
# print()

print("How could we tell Pandas that the result of sum should be called total_amount, and the result of mean should be called avg_amount? ")
print(transaction_df.groupby("customer_id").agg(
    total_amount = ("amount","sum"),
    avg_amount = ("amount","mean"),
    transaction_count = ("customer_id","size")
))
print()

# print("number of unique values: ")
# print(transaction_df.groupby("customer_id")["country"].nunique())
# print()

customer_features = transaction_df.groupby("customer_id").agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    transaction_count=("customer_id", "size"),
    unique_country_count=("country","nunique"),
    unique_channel_count=("channel","nunique"),
    country=("country","first"),
    channel=("channel","first"),
    largest_transaction=("amount","max"),
    smallest_transaction=("amount","min"),
    
)


transaction_range = customer_features["largest_transaction"] - customer_features["smallest_transaction"]
customer_features["transaction_range"] = transaction_range
print("Custome Transaction DataFrame:")
print(customer_features)
print()

# print("Select only customers where total_amount > 1500: ")
# print(customer_features.loc[customer_features.loc[:,"total_amount"] > 1500])
# print()

# print("Find customers who have both: total_amount > 1500 and transaction_count >= 2")
# print(customer_features.loc[(customer_features.loc[:,"total_amount"] > 1500) & (customer_features.loc[:,"transaction_count"] >= 2)])
# print()

# print("Flag customers who have transactions from more than one country ")
# print(customer_features.loc[customer_features.loc[:,"unique_country_count"] > 1])
# print()

# print("Find customers who have both: total_amount > 1500 and unique_country_count > 1")
# print(customer_features.loc[(customer_features.loc[:,"total_amount"] > 1500) & (customer_features.loc[:,"unique_country_count"] > 1)])
# print()

# print("Flag customers who have used more than one country AND more than one transaction channel.")
# print(customer_features.loc[(customer_features.loc[:,"unique_country_count"] > 1) & (customer_features.loc[:,"unique_channel_count"] > 1)])
# print()

# print("A customer should be considered high-risk if: total transaction amount > 1500, has used more than one country and has used more than one transaction channel")
# print(customer_features.loc[(customer_features.loc[:,"total_amount"] > 1500) & (customer_features.loc[:,"unique_country_count"] > 1) & (customer_features.loc[:,"unique_channel_count"] > 1)])
# print()

# print("A customer should be considered high-risk if: total transaction amount > 1500, has used more than one country and Their transaction_range is greater than 400")
# print(customer_features.loc[(customer_features.loc[:,"total_amount"] > 1500) & (customer_features.loc[:,"unique_country_count"] > 1) & (customer_features.loc[:,"transaction_range"] > 400)])
# print()

