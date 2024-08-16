import pandas as pd

def extract_data(file_path):
    """
    Extract data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file to be read.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the extracted data.
    """
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    """
    Main execution block.

    This block extracts data from the specified CSV file, saves it to a new CSV file
    in the 'data/extracted' directory, and prints a success message.
    """
    file_path = 'data/raw/Cyber Security Breaches.csv'
    data = extract_data(file_path)
    data.to_csv('data/extracted/cyber_security_breaches.csv', index=False)
    print("Data extracted successfully.")