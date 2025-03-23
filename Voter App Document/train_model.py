from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

# Load dataset
df = pd.read_csv("voter_turnout_data.csv")

# Encode categorical variables
label_encoders = {}
categorical_columns = ["weather", "day_of_week", "population_density"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])  # Convert categories to numbers
    label_encoders[col] = le  # Save encoders for future use

# Split features & target variable
X = df.drop(columns=["voter_turnout"])  # Features
y = df["voter_turnout"]  # Target variable

# After training, save feature names used for future prediction
joblib.dump(X.columns.tolist(), "feature_columns.pkl")  # Save column names

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "voter_turnout_model.pkl")

# Save encoders for later use
joblib.dump(label_encoders, "label_encoders.pkl")

print("Model training complete. Saved as voter_turnout_model.pkl")