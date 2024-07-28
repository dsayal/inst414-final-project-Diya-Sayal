import pandas as pd

def load_extracted_data(file_path):
    """
    Load extracted data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file to be read.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Clean the data by removing missing values and duplicates.

    Parameters:
    data (pd.DataFrame): The DataFrame to be cleaned.

    Returns:
    pd.DataFrame: A cleaned pandas DataFrame.
    """
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    # Additional cleaning steps as required
    return data

if __name__ == "__main__":
    """
    Main execution block.

    This block loads extracted data from the specified CSV file, cleans it,
    saves the cleaned data to a new CSV file in the 'data/processed' directory,
    and prints a success message.
    """
    file_path = 'data/extracted/cyber_security_breaches.csv'
    data = load_extracted_data(file_path)
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('data/processed/cleaned_cyber_security_breaches.csv', index=False)
    print("Data transformed and loaded successfully.")