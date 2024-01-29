import pandas as pd

# Load the dataset
file_path = 'C:\Users\PC TOUR\Desktop\CO2_TP\CO2_per_capita.csv'
co2_data = pd.read_csv(file_path, sep=';')

# Displaying the first few rows of the dataset to understand its contents
co2_data.head()
