import pandas as pd

def load_data(source_path):
    """
    Loads the processed data for analysis.
    
    Parameters:
    source_path (str): The path to the processed data file.
    
    Returns:
    pd.DataFrame: The loaded data frame.
    """
    try:
        data = pd.read_csv(source_path)
        print(f"Data loaded from {source_path}")
        return data
    except Exception as e:
        print(f"Error during loading: {e}")
        return None

if __name__ == "__main__":
    source_file_path = 'data/processed/processed_data.csv' #update
    data = load_data(source_file_path)
    if data is not None:
        print(data.head())  # Display the first few rows of the loaded data