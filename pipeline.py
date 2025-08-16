import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score

# Load dataset (placeholder: use any churn dataset)
data = pd.read_csv("customer_data.csv")
X = data.drop("churn", axis=1)
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train churn prediction model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict_proba(X_test)[:,1]
auc = roc_auc_score(y_test, y_pred)

# High-risk precision evaluation
y_label = (y_pred > 0.9).astype(int)
precision = precision_score(y_test, y_label)

# Anomaly detection on full dataset
iso = IsolationForest(contamination=0.05, random_state=42)
data["anomaly_flag"] = iso.fit_predict(X)
data["churn_probability"] = clf.predict_proba(X)[:,1]

# Export results to CSV for Power BI
data.to_csv("customer_churn_predictions.csv", index=False)

print(f"AUC: {auc:.2f}, High-risk precision: {precision:.2f}")
print("Predictions exported to customer_churn_predictions.csv")
