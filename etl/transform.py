import pandas as pd
import os

def transform_databreaches_data():
    """
    Transform the databreaches data by performing data cleaning and date conversion.
    
    This function:
    1. Loads raw databreaches data from 'data/extracted/databreaches_data.csv'.
    2. Drops rows with missing values.
    3. Converts 'date_column' to datetime format if it exists.
    4. Saves the transformed data to 'data/processed/databreaches_data_transformed.csv'.

    Returns:
        pd.DataFrame: The cleaned and transformed databreaches data.
    """
    # Load the raw data
    df = pd.read_csv('data/extracted/databreaches_data.csv')

    # Clean the data by dropping rows with missing values
    df_cleaned = df.dropna()

    # Convert 'date_column' to datetime format if it exists
    if 'date_column' in df_cleaned.columns:
        df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

    # Save the transformed data
    os.makedirs('data/processed', exist_ok=True)
    df_cleaned.to_csv('data/processed/databreaches_data_transformed.csv', index=False)

    print("Databreaches data transformed and saved to 'data/processed/databreaches_data_transformed.csv'.")
    return df_cleaned

def transform_cyberbreaches_data():
    """
    Transform the cyberbreaches data by performing data cleaning and date conversion.
    
    This function:
    1. Loads raw cyberbreaches data from 'data/extracted/cyberbreaches_data.csv'.
    2. Drops rows with missing values.
    3. Converts 'date_column' to datetime format if it exists.
    4. Saves the transformed data to 'data/processed/cyberbreaches_data_transformed.csv'.

    Returns:
        pd.DataFrame: The cleaned and transformed cyberbreaches data.
    """
    # Load the raw data
    df = pd.read_csv('data/extracted/cyberbreaches_data.csv')

    # Clean the data by dropping rows with missing values
    df_cleaned = df.dropna()

    # Convert 'date_column' to datetime format if it exists
    if 'date_column' in df_cleaned.columns:
        df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

    # Save the transformed data
    os.makedirs('data/processed', exist_ok=True)
    df_cleaned.to_csv('data/processed/cyberbreaches_data_transformed.csv', index=False)

    print("Cyberbreaches data transformed and saved to 'data/processed/cyberbreaches_data_transformed.csv'.")
    return df_cleaned

def main():
    """
    Main function to transform both databreaches and cyberbreaches data.
    """
    transform_databreaches_data()
    transform_cyberbreaches_data()

if __name__ == "__main__":
    main()
