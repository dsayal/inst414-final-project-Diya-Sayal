import pandas as pd
import os

def extract_databreaches_data():
    """
    Extract data from a CSV file.
    """
   
    csv_file_path = '/Users/diyasayal/Desktop/INST414/databreaches.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Save the DataFrame to a CSV file in the 'data/extracted' directory
    os.makedirs('data/extracted', exist_ok=True)
    df.to_csv('data/extracted/databreaches_data.csv', index=False)

    return df

def extract_cyberbreaches_data():
    """
    Extract data from a CSV file.
    """
    # Path to the CSV file (update with your actual file path)
    csv_file_path = '/Users/diyasayal/Desktop/INST414/cybersecuritybreaches.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Save the DataFrame to a CSV file in the 'data/extracted' directory
    os.makedirs('data/extracted', exist_ok=True)
    df.to_csv('data/extracted/cyberbreaches_data.csv', index=False)

    return df

def main():
    # Extract data from the CSV files
    databreaches_data = extract_databreaches_data()
    cyberbreaches_data = extract_cyberbreaches_data()

if __name__ == "__main__":
    main()
