
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


print("\nUPDATED ENRICHED TRANSACTIONS")
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
Are all three columns numeric?
"""
print(
    "amount: ",
    risk_enriched_transactions["amount"].dtype
)

print()

print(
    "Acoount age: ",
    risk_enriched_transactions["account_age_days"].dtype
)

print()


print(
    "Fraud Reports: ",
    risk_enriched_transactions["previous_fraud_reports"].dtype
)

print()

print("How many missing values are there in each of the three feature columns?",end='\n')

print(
    "Amount: ",
    risk_enriched_transactions["amount"].isna().any()
)

print()

print(
    "Account Age Days: ",
    risk_enriched_transactions["account_age_days"].isna().any()
)

print()

print(
    "Previous Fraud Reports: ",
    risk_enriched_transactions["previous_fraud_reports"].isna().any()
)

print()

print("Which transaction IDs have a missing account age?",end='\n')

missing_account_age = risk_enriched_transactions["account_age_days"].isna()
print(risk_enriched_transactions.loc[missing_account_age])
print()

print("What is the actual account age of customer C004 in our customer dataset: unknown, zero, or a known number?", end="\n")
print(risk_enriched_transactions.loc[missing_account_age]["account_age_days"])
print()

"""
Your task: Create a new DataFrame named training_data that contains only rows where account_age_days is available.
"""
# Keep only transactions with a known account age
training_data = risk_enriched_transactions.loc[risk_enriched_transactions["account_age_days"].notna()]
print("\nTRAINING DATA")
print(training_data)
print("\nNumber of training rows: ",len(training_data))

# Select numeric features for the model
feature_columns = [
    "amount",
    "account_age_days",
    "previous_fraud_reports"
]

X = training_data[feature_columns]
print("\nFEATURE DATAFRAME")
print(X)
print("\nFEATURE SHAPE: ",X.shape)
print()
print("FEATURE DATA TYPES: ")
print(X.dtypes)
print()

# Convert the feature DataFrame into a NumPy array
X_numpy = X.to_numpy()

print("\nNUMPY FEATURE MATRIX")
print(X_numpy)

print("\nNUMPY MATRIX SHAPE:", X_numpy.shape)
print("\nNUMPY MATRIX DATA TYPE:", X_numpy.dtype)

print("\nFEATURE MINIMUMS:")
print(X.min())

print("\nFEATURE MAXIMUMS:")
print(X.max())

# Step 8: Min-Max Scaling
X_scaled = (X - X.min()) / (X.max() - X.min())

print("\nSCALED FEATURES:")
print(X_scaled)

print("\nSCALED FEATURE MINIMUMS:")
print(X_scaled.min())

print("\nSCALED FEATURE MAXIMUMS:")
print(X_scaled.max())