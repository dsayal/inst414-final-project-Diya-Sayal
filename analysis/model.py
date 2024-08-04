import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_and_save_model():
    """
    Train a model and save it to a file.
    """
    # Load data
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    
    # Convert categorical features to numeric using LabelEncoder
    le = LabelEncoder()
    df_encoded = df.apply(le.fit_transform)  # Encode all columns

    # Split data
    X = df_encoded.drop(columns=['Organization type'])
    y = df_encoded['Organization type']

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
    
    # Convert categorical features to numeric using the same LabelEncoder
    le = LabelEncoder()
    df_encoded = df.apply(le.fit_transform)

    X_test = df_encoded.drop(columns=['Organization type'])
    y_true = df_encoded['Organization type']

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate the model
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Databreaches Data Confusion Matrix:\n", conf_matrix)

    report = classification_report(y_true, y_pred, zero_division=0)
    print("Databreaches Data Classification Report:\n", report)





