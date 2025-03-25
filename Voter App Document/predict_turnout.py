import joblib
import pandas as pd

# Load trained model
model = joblib.load("voter_turnout_model.pkl")

# Load saved label encoders
label_encoders = joblib.load("label_encoders.pkl")

# Load feature names used during training
feature_names = joblib.load("feature_columns.pkl")

# Define new election data for prediction
new_data = pd.DataFrame({
    "election_id": [1], 
    "age_18_25": [3],  
    "age_26_40": [4],  
    "age_41_60": [93],  
    "age_60_plus": [100],  
    "weather": ["Sunny"],  
    "day_of_week": ["Weekend"],  
    "previous_turnout": [93],  
    "population_density": ["Urban"]  
})

# Convert categorical columns using saved LabelEncoders
for col in label_encoders:
    new_data[col] = label_encoders[col].transform(new_data[col])

# Ensure all required columns are present
for col in feature_names:
    if col not in new_data:
        new_data[col] = 0  # Add missing columns with default value

# Reorder columns to match training data
new_data = new_data[feature_names]

# Predict voter turnout
predicted_turnout = model.predict(new_data)

print(f"Predicted Voter Turnout: {predicted_turnout[0]:.2f}%")