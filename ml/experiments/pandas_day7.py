
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
print()

"""
Adding new data in left table that is transaction_df
"""

new_transaction = pd.DataFrame({
    "transaction_id":["T107"],
    "customer_id":["C004"],
    "amount":[9000],
    "country":["IN"],
    "channel":["WEB"]
})

transaction_df = pd.concat(
    [transaction_df,new_transaction],
    ignore_index=True
)


print("\nUPDATED TRANSACTIONS")
print(transaction_df)
print()

updated_enriched_transactions = pd.merge(
    transaction_df,
    customer_df,
    on="customer_id",
    how="left"
)


print("\nUpdated ENRICHED TRANSACTIONS")
print(updated_enriched_transactions)
print()

risk_profile_data = {
    "customer_id": ["C001", "C002", "C003", "C004"],
    "risk_level": ["LOW", "MEDIUM", "LOW", "HIGH"],
    "previous_fraud_reports": [0, 1, 0, 3],
}

risk_profile_df = pd.DataFrame(risk_profile_data)

print("\nCUSTOMER RISK PROFILES")
print(risk_profile_df)
print()

risk_enriched_transactions = pd.merge(
    updated_enriched_transactions,
    risk_profile_df,
    on="customer_id",
    how="left"
)

print("\nRISK-ENRICHED TRANSACTIONS")
print(risk_enriched_transactions)
print()

"""
check the number of rows in that DataFrame
"""
print("Number of the rows: ")
print(len(risk_enriched_transactions))
print()

"""
Challenge 4 — Check 2: Are transaction IDs unique?
Our next business requirement is:
Every transaction must have a unique transaction_id. 
If an ID appears more than once, we need to investigate before trusting the risk-engine dataset.
"""

print(
    "Any duplicate transaction IDs:",
    risk_enriched_transactions["transaction_id"].duplicated().any()
    )
print()

print(
    "Transactions missing customer segment:",
    risk_enriched_transactions['customer_segment'].isna().sum()
)

print()

print(
    "Transactions missing risk level:",
    risk_enriched_transactions["risk_level"].isna().sum()
)

