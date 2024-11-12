import pandas as pd

# Select columns for frequency analysis
columns_to_analyze = ["Source", "Destination", "Protocol"]

# Read the CSV file using pandas
try:
  df = pd.read_csv("IN300_Dataset1.csv", usecols=columns_to_analyze)
except FileNotFoundError:
  print("Error: File 'IN300_Dataset1.csv' not found. Please check the file path.")
  exit()

# Loop through each column and calculate frequency counts
for col in columns_to_analyze:
  counts = df[col].value_counts().sort_values(ascending=False)
  print(f"{col} frequency count (descending):")
  print(counts)
  print()
