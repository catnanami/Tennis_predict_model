from statsmodels.sandbox.stats.runs import runstest_1samp
import pandas as pd
import numpy as np

np.random.seed(42)

# Generate stochastic sequence
Stochastic_sequence = np.random.choice([0, 1], size=10000, p=[0.5, 0.5])

# Read files and data
file_path = 'C_Wimbledon_featured_matches.csv'
df = pd.read_csv(file_path)
original_data = df.iloc[1:1001, 15].tolist()

# Data processing
binary_data = [1 if x == 1 else 0 for x in original_data]

print(runstest_1samp(binary_data))
print(runstest_1samp(Stochastic_sequence))