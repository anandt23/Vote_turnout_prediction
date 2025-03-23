import joblib
import pandas as pd

# Load the trained model
model = joblib.load("voter_turnout_model.pkl")

# Define new election data for prediction
new_data = pd.DataFrame({
    "election_id": [4], 
    "age_18_25": [20],  
    "age_26_40": [4],  
    "age_41_60": [3],  
    "age_60_plus": [1],  
    "weather": ["Sunny"],  
    "day_of_week": ["Weekend"],  
    "previous_turnout": [63],  
    "population_density": ["Rural"]  
})

# Convert categorical columns
new_data = pd.get_dummies(new_data)

# Load feature names used during training
feature_names = joblib.load("feature_columns.pkl")

# Ensure all required columns are present
for col in feature_names:
    if col not in new_data:
        new_data[col] = 0  # Add missing columns with default value

# Reorder columns to match training data
new_data = new_data[feature_names]

# Predict voter turnout
predicted_turnout = model.predict(new_data)

print(f"Predicted Voter Turnout: {predicted_turnout[0]:.2f}%")