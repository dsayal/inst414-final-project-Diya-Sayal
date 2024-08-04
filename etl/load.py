import pandas as pd

def load_databreaches_data():
    """
    Load the transformed databreaches data from the 'data/processed' directory.
    
    This function reads data from the CSV file 'databreaches_data_transformed.csv' 
    and prints a success message.

    Returns:
        pd.DataFrame: The DataFrame containing the transformed databreaches data.
    """
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    print("Databreaches data loaded successfully.")
    return df

def load_cyberbreaches_data():
    """
    Load the transformed cyberbreaches data from the 'data/processed' directory.
    
    This function reads data from the CSV file 'cyberbreaches_data_transformed.csv' 
    and prints a success message.

    Returns:
        pd.DataFrame: The DataFrame containing the transformed cyberbreaches data.
    """
    df = pd.read_csv('data/processed/cyberbreaches_data_transformed.csv')
    print("Cyberbreaches data loaded successfully.")
    return df

def main():
    """
    Main function to load both transformed databreaches and cyberbreaches data.
    """
    load_databreaches_data()
    load_cyberbreaches_data()

if __name__ == "__main__":
    main()

