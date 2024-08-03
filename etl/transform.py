import pandas as pd
import os

def transform_databreaches_data():
    """
    Transform the databreaches data.
    """
    # Load the raw data
    df = pd.read_csv('data/extracted/databreaches_data.csv')

    # Example transformation: Remove rows with missing values
    df_cleaned = df.dropna()

    # Example transformation: Convert date columns to datetime
    # Replace 'date_column' with actual column names
    if 'date_column' in df_cleaned.columns:
        df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

    # Save the transformed data
    os.makedirs('data/processed', exist_ok=True)
    df_cleaned.to_csv('data/processed/databreaches_data_transformed.csv', index=False)

    print("Databreaches data transformed and saved to 'data/processed/databreaches_data_transformed.csv'.")
    return df_cleaned

def transform_cyberbreaches_data():
    """
    Transform the cyberbreaches data.
    """
    # Load the raw data
    df = pd.read_csv('data/extracted/cyberbreaches_data.csv')

    # Example transformation: Remove rows with missing values
    df_cleaned = df.dropna()

    # Example transformation: Convert date columns to datetime
    # Replace 'date_column' with actual column names
    if 'date_column' in df_cleaned.columns:
        df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

    # Save the transformed data
    os.makedirs('data/processed', exist_ok=True)
    df_cleaned.to_csv('data/processed/cyberbreaches_data_transformed.csv', index=False)

    print("Cyberbreaches data transformed and saved to 'data/processed/cyberbreaches_data_transformed.csv'.")
    return df_cleaned

def main():
    transform_databreaches_data()
    transform_cyberbreaches_data()

if __name__ == "__main__":
    main()