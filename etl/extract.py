import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset_name, destination_path='data/extracted'):
    """
    Downloads a dataset from Kaggle using the Kaggle API.

    Args:
        dataset_name (str): The Kaggle dataset name in the format 'username/dataset-name'.
        destination_path (str): The path where the dataset will be downloaded. Default is 'data/extracted'.
    """
    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    # Download the dataset
    api.dataset_download_files(dataset_name, path=destination_path, unzip=True)

def extract_databreaches_data(csv_filename='databreaches.csv', destination_path='data/extracted'):
    """
    Extract data from a CSV file.

    Args:
        csv_filename (str): The name of the CSV file to extract.
        destination_path (str): The path where the dataset will be downloaded and extracted.
    """
    csv_file_path = os.path.join(destination_path, csv_filename)

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist. Please check the file path.")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Save the DataFrame to a CSV file in the 'data/extracted' directory
    os.makedirs(destination_path, exist_ok=True)
    df.to_csv(os.path.join(destination_path, 'databreaches_data.csv'), index=False)

    return df

def extract_cyberbreaches_data(csv_filename='cybersecuritybreaches.csv', destination_path='data/extracted'):
    """
    Extract data from a CSV file.

    Args:
        csv_filename (str): The name of the CSV file to extract.
        destination_path (str): The path where the dataset will be downloaded and extracted.
    """
    csv_file_path = os.path.join(destination_path, csv_filename)

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist. Please check the file path.")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Save the DataFrame to a CSV file in the 'data/extracted' directory
    os.makedirs(destination_path, exist_ok=True)
    df.to_csv(os.path.join(destination_path, 'cyberbreaches_data.csv'), index=False)

    return df

def main():
    # Download data from Kaggle
    download_kaggle_dataset('username/dataset-name', 'data/extracted')

    # Extract data from the CSV files
    databreaches_data = extract_databreaches_data()
    cyberbreaches_data = extract_cyberbreaches_data()

if __name__ == "__main__":
    main()



