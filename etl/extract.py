import pandas as pd
import os

def extract_databreaches_data():
    """
    Extract data from the 'databreaches.csv' file and save it to the 'data/extracted' directory.
    
    This function performs the following steps:
    1. Reads data from a CSV file located at '/Users/diyasayal/Desktop/INST414/databreaches.csv'.
    2. Saves the extracted data to a new CSV file in the 'data/extracted' directory.

    Returns:
        pd.DataFrame: The DataFrame containing the extracted data.
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
    Extract data from the 'cybersecuritybreaches.csv' file and save it to the 'data/extracted' directory.
    
    This function performs the following steps:
    1. Reads data from a CSV file located at '/Users/diyasayal/Desktop/INST414/cybersecuritybreaches.csv'.
    2. Saves the extracted data to a new CSV file in the 'data/extracted' directory.

    Returns:
        pd.DataFrame: The DataFrame containing the extracted data.
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
    """
    Main function to extract data from both CSV files.
    """
    # Extract data from the CSV files
    databreaches_data = extract_databreaches_data()
    cyberbreaches_data = extract_cyberbreaches_data()

if __name__ == "__main__":
    main()

