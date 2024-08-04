import pandas as pd
import os

def extract_databreaches_data():
    """
    Extract data from a CSV file.
    """
    csv_file_path = '/Users/diyasayal/Desktop/INST414/databreaches.csv'

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist. Please check the file path.")
    
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
    csv_file_path = '/Users/diyasayal/Desktop/INST414/cybersecuritybreaches.csv'

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist. Please check the file path.")
    
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


