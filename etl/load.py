import pandas as pd

def load_databreaches_data():
    """
    Load the transformed databreaches data.
    """
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    print("Databreaches data loaded successfully.")
    return df

def load_cyberbreaches_data():
    """
    Load the transformed cyberbreaches data.
    """
    df = pd.read_csv('data/processed/cyberbreaches_data_transformed.csv')
    print("Cyberbreaches data loaded successfully.")
    return df

def main():
    load_databreaches_data()
    load_cyberbreaches_data()

if __name__ == "__main__":
    main()
