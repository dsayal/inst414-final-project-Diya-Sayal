#creating reference tables
import pandas as pd
import os

# Define the file paths
data_breaches_path = '/Users/diyasayal/Desktop/INST414/DataBreaches_DataDictionary.csv'
cyberbreach_data_path = '/Users/diyasayal/Desktop/INST414/CyberBreaches_DataDictionary.csv'

# Create the reference-tables directory if it doesn't exist
reference_tables_dir = '/Users/diyasayal/Desktop/INST414/reference-tables'
os.makedirs(reference_tables_dir, exist_ok=True)

# Load the CSV files into DataFrames
data_breaches_df = pd.read_csv(data_breaches_path)
cyberbreach_data_df = pd.read_csv(cyberbreach_data_path)

# Display the first few rows of the DataFrames to ensure they've loaded correctly
print(data_breaches_df.head())
print(cyberbreach_data_df.head())

# Create reference tables
def create_reference_table(df, file_name):
    reference_table = pd.DataFrame({
        'attribute_name': df.columns,
        'description': ['Description of ' + col for col in df.columns],
        'data_type': [str(df[col].dtype) for col in df.columns],
        'example_value': [df[col].dropna().iloc[0] if not df[col].dropna().empty else 'N/A' for col in df.columns],
        'unit': ['' for _ in df.columns]  # Add units if applicable
    })
    reference_table_path = os.path.join(reference_tables_dir, file_name)
    reference_table.to_csv(reference_table_path, index=False)
    print(f"Reference table saved to {reference_table_path}")

# Create reference tables for each dataset
create_reference_table(data_breaches_df, 'data_breaches_reference.csv')
create_reference_table(cyberbreach_data_df, 'CyberBreaches_DataDictionary.csv')
