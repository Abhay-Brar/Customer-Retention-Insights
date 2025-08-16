import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

n_rows = 1000

data = {
    "CustomerID": np.arange(1, n_rows + 1),
    "Age": np.random.randint(18, 70, n_rows),
    "Income": np.random.randint(25000, 120000, n_rows),
    "Tenure": np.random.randint(1, 48, n_rows),
    "NumProducts": np.random.randint(1, 5, n_rows),
    "HasCreditCard": np.random.choice([0, 1], n_rows, p=[0.3, 0.7]),
    "IsActiveMember": np.random.choice([0, 1], n_rows, p=[0.4, 0.6]),
    "Churn": np.random.choice([0, 1], n_rows, p=[0.75, 0.25])
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_data.csv", index=False)
print("1000 rows of sample data written to sample_data.csv")
