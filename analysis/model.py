import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_processed_data(file_path):
    """
    Load the processed data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the processed data.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the loaded data.
    """
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    """
    Train a RandomForestClassifier model on the provided data.

    This function splits the data into training and test sets, trains a RandomForestClassifier
    on the training data, and evaluates its accuracy on the test data.

    Parameters:
    data (pd.DataFrame): The processed data containing features and target.

    Returns:
    model (RandomForestClassifier): The trained RandomForestClassifier model.
    accuracy (float): The accuracy score of the model on the test data.
    """
    # Example analysis
    X = data.drop('Location_of_Breached_Information', axis=1)
    y = data['Location_of_Breached_Information']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

if __name__ == "__main__":
    """
    Main execution block.

    This block loads the processed data, trains the RandomForestClassifier model,
    and prints the model's accuracy.
    """
    file_path = 'data/processed/cleaned_cyber_security_breaches.csv'
    data = load_processed_data(file_path)
    model, accuracy = train_model(data)
    print(f'Model Accuracy: {accuracy}')