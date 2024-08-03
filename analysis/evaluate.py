import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import joblib
import os

def train_and_save_model():
    """
    Train a model and save it to a file.
    """
    # Load data
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    X = df.drop(columns=['Organization type'])  # Assuming all columns except target are features
    y = df['Organization type']  # Target variable

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'model/databreaches_model.pkl')

def evaluate_databreaches_model():
    """
    Evaluate metrics for the databreaches data.
    """
    model_path = 'model/databreaches_model.pkl'
    if not os.path.exists(model_path):
        print(f"Model file '{model_path}' does not exist. Please train the model first.")
        return

    # Load the trained model
    model = joblib.load(model_path)

    # Load test data
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    print("Data columns:", df.columns)  # Debug print to check columns

    X_test = df.drop(columns=['Organization type'])  # Features
    y_true = df['Organization type']  # True labels

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate the model
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Databreaches Data Confusion Matrix:\n", conf_matrix)

    report = classification_report(y_true, y_pred, zero_division=0)
    print("Databreaches Data Classification Report:\n", report)

def main():
    train_and_save_model()
    
    evaluate_databreaches_model()

if __name__ == "__main__":
    main()



