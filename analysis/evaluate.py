import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def evaluate_databreaches_model():
    """
    Evaluate the performance of the trained RandomForest model on the test dataset.
    
    The function performs the following steps:
    1. Checks if the model file exists and loads it.
    2. Loads the LabelEncoder and applies it to encode categorical features.
    3. Loads the test dataset from a CSV file.
    4. Splits the data into features and target variables.
    5. Predicts the target values using the loaded model.
    6. Evaluates the model's performance using confusion matrix and classification report.
    """
    model_path = 'outputs/model/databreaches_model.pkl'
    le_path = 'outputs/model/label_encoders.pkl'
    
    if not os.path.exists(model_path):
        print(f"Model file '{model_path}' does not exist. Please train the model first.")
        return

    if not os.path.exists(le_path):
        print(f"LabelEncoder file '{le_path}' does not exist. Please train the model first.")
        return

    # Load the trained model
    model = joblib.load(model_path)
    
    # Load the LabelEncoders
    le_dict = joblib.load(le_path)

    # Load test data
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    
    # Encode categorical features using the same LabelEncoders
    df_encoded = df.copy()
    for column in df_encoded.select_dtypes(include=['object']).columns:
        if column in le_dict:
            df_encoded[column] = le_dict[column].transform(df_encoded[column])
        else:
            print(f"Warning: No LabelEncoder found for column '{column}'.")
            df_encoded[column] = pd.factorize(df_encoded[column])[0]  # Fallback if column not found in le_dict

    X_test = df_encoded.drop(columns=['Organization type'])
    y_true = df_encoded['Organization type']

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate the model
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Databreaches Data Confusion Matrix:\n", conf_matrix)

    # Ensure the metrics directory exists
    os.makedirs('data/outputs/metrics', exist_ok=True)

    # Save confusion matrix
    pd.DataFrame(conf_matrix).to_csv('data/outputs/metrics/confusion_matrix.csv')

    report = classification_report(y_true, y_pred, zero_division=0)
    print("Databreaches Data Classification Report:\n", report)

    # Save classification report
    with open('data/outputs/metrics/classification_report.txt', 'w') as f:
        f.write(report)











