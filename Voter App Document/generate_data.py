import pandas as pd
import numpy as np
import random

# Function to generate synthetic data
def generate_voter_turnout_data(num_samples=1000):
    data = {
        "election_id": np.random.randint(1, 10, num_samples),
        "age_18_25": np.random.uniform(10, 40, num_samples),  # percentage
        "age_26_40": np.random.uniform(20, 50, num_samples),
        "age_41_60": np.random.uniform(15, 40, num_samples),
        "age_60_plus": np.random.uniform(5, 30, num_samples),
        "weather": np.random.choice(["Sunny", "Rainy", "Snowy", "Cloudy"], num_samples),
        "day_of_week": np.random.choice(["Weekday", "Weekend"], num_samples),
        "previous_turnout": np.random.uniform(40, 80, num_samples),
        "population_density": np.random.choice(["Urban", "Rural"], num_samples),
        "voter_turnout": np.random.uniform(40, 90, num_samples)  # Target variable (percentage turnout)
    }
    
    return pd.DataFrame(data)

# Generate and save dataset
df = generate_voter_turnout_data(1000)
df.to_csv("voter_turnout_data.csv", index=False)

print("Synthetic voter turnout dataset generated and saved as 'voter_turnout_data.csv'.")