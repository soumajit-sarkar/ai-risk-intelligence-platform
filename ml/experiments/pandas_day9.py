
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


# Step 3: Validate transaction IDs

missing_transaction_ids = transaction_df["transaction_id"].isna().sum()
duplicate_transaction_ids = transaction_df["transaction_id"].duplicated().sum()

print("\nTRANSACTION ID VALIDATION")
print("Missing transaction IDs:", missing_transaction_ids)
print("Duplicate transaction IDs:", duplicate_transaction_ids)

# Step 4: Validate transaction amounts
missing_amounts = transaction_df["amount"].isna().sum()
invalid_amounts = (transaction_df["amount"] <= 0).sum()

print("\nTRANSACTION AMOUNT VALIDATION")
print("Missing transaction amounts:", missing_amounts)
print("Zero or negative transaction amounts:", invalid_amounts)
print()



# Step 5: Validate customer references

known_customer_ids = customer_df["customer_id"]

missing_customer_reference = ~transaction_df["customer_id"].isin(
    known_customer_ids
)

transactions_without_customer = transaction_df.loc[
    missing_customer_reference
]

print("\nCUSTOMER REFERENCE VALIDATION")
print("Transactions without a customer record:", len(transactions_without_customer))
print(transactions_without_customer)
print()


# Step 6: Validate risk-profile references

known_risk_customer_ids = risk_profile_df["customer_id"]

missing_risk_profile = ~transaction_df["customer_id"].isin(
    known_risk_customer_ids
)

transactions_without_risk_profile = transaction_df.loc[
    missing_risk_profile
]

print("\nRISK PROFILE REFERENCE VALIDATION")
print("Transactions without a risk profile:", len(transactions_without_risk_profile))
print(transactions_without_risk_profile)
print()


# Step 7: Enrich transactions with customer and risk information

customer_enriched = transaction_df.merge(
    customer_df,
    on="customer_id",
    how="left"
)

risk_enriched = customer_enriched.merge(
    risk_profile_df,
    on="customer_id",
    how="left"
)

print("\nFINAL RISK-ENRICHED DATASET")
print(risk_enriched)

print("\nTOTAL TRANSACTIONS:", len(risk_enriched))
print("MISSING CUSTOMER SEGMENTS:", risk_enriched["customer_segment"].isna().sum())
print("MISSING ACCOUNT AGES:", risk_enriched["account_age_days"].isna().sum())
print("MISSING RISK LEVELS:", risk_enriched["risk_level"].isna().sum())
print()


# Step 8: Flag incomplete customer information

risk_enriched["customer_data_incomplete"] = (
    risk_enriched["customer_segment"].isna()
    | risk_enriched["account_age_days"].isna()
)

print("\nCUSTOMER DATA QUALITY CHECK")
print(
    risk_enriched[
        ["transaction_id", "customer_data_incomplete"]
    ]
)
print(
    "\nTransactions with incomplete customer data:",
    risk_enriched["customer_data_incomplete"].sum()
)
print()

risk_enriched["high_value_transaction"] = (
    risk_enriched["amount"] >= 10000
)

print("\nHIGH-VALUE TRANSACTION FEATURE")
print(
    risk_enriched[
        ["transaction_id", "amount", "high_value_transaction"]
    ]
)
print()

risk_enriched["customer_has_fraud_history"] = (
    risk_enriched["previous_fraud_reports"] > 0
)

print("\nCUSTOMER FRAUD HISTORY FEATURE")
print(
    risk_enriched[
        [
            "transaction_id",
            "customer_id",
            "previous_fraud_reports",
            "customer_has_fraud_history",
        ]
    ]
)
print()


risk_enriched["requires_risk_review"] = (
    risk_enriched["high_value_transaction"]
    | risk_enriched["customer_has_fraud_history"]
)

print("\nRISK REVIEW INDICATOR")
print(
    risk_enriched[
        [
            "transaction_id",
            "high_value_transaction",
            "customer_has_fraud_history",
            "requires_risk_review",
        ]
    ]
)
print()


print("\nFINAL RISK ENGINE SUMMARY")
print("Total transactions:", len(risk_enriched))
print("Transactions requiring review:", risk_enriched["requires_risk_review"].sum())
print("High-value transactions:", risk_enriched["high_value_transaction"].sum())
print("Transactions with fraud history:", risk_enriched["customer_has_fraud_history"].sum())
print("Transactions with incomplete customer data:", risk_enriched["customer_data_incomplete"].sum())
