import os
import subprocess
import zipfile

def download_kaggle_dataset(dataset_command, destination_path):
    """
    Download a dataset from Kaggle using the Kaggle CLI command.
    """
    print(f"Downloading dataset using command: {dataset_command}")
    
    try:
        # Run the Kaggle CLI command to download the dataset
        result = subprocess.run(dataset_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")

def unzip_file(zip_path, extract_to):
    """
    Unzip a downloaded dataset file.
    """
    print(f"Unzipping file: {zip_path}")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Unzipped successfully to: {extract_to}")
    except Exception as e:
        print(f"An error occurred while unzipping: {str(e)}")

def extract_databreaches_data():
    """
    Function to handle the extraction of the data breaches dataset.
    """
    data_breach_command = 'kaggle datasets download -d thedevastator/data-breaches-a-comprehensive-list'
    destination_path = 'data/extracted'
    download_kaggle_dataset(data_breach_command, destination_path)
    
    for file_name in os.listdir(destination_path):
        file_path = os.path.join(destination_path, file_name)
        if file_path.endswith('.zip'):
            unzip_file(file_path, destination_path)

def extract_cyberbreaches_data():
    """
    Function to handle the extraction of the cyber breaches dataset.
    """
    cybersecurity_breach_command = 'kaggle datasets download -d alukosayoenoch/cyber-security-breaches-data'
    destination_path = 'data/extracted'
    download_kaggle_dataset(cybersecurity_breach_command, destination_path)
    
    for file_name in os.listdir(destination_path):
        file_path = os.path.join(destination_path, file_name)
        if file_path.endswith('.zip'):
            unzip_file(file_path, destination_path)

if __name__ == "__main__":
    extract_databreaches_data()
    extract_cyberbreaches_data()







