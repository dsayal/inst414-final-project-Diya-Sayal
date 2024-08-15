import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set Kaggle API credentials using environment variables
os.environ['KAGGLE_USERNAME'] = 'diyasayal'
os.environ['KAGGLE_KEY'] = '798a3835d06a26842f1144c987738b75'

# Initialize and authenticate the Kaggle API
api = KaggleApi()
api.authenticate()

# Example usage of Kaggle API
def download_dataset():
    api.dataset_download_files('dataset-owner/dataset-name', path='data/extracted', unzip=True)

if __name__ == "__main__":
    download_dataset()
