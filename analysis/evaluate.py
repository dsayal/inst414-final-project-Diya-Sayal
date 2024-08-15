import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_and_save_model():
    """
    Train a RandomForest model using the processed breach data and save it to a file.
    
    The function performs the following steps:
    1. Loads the transformed dataset from a CSV file.
    2. Encodes categorical features to numeric values using LabelEncoder.
    3. Splits the data into training and testing sets.
    4. Initializes and trains a RandomForestClassifier model.
    5. Saves the trained model and LabelEncoder to files.
    """
    # Load data
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    
    # Initialize LabelEncoder and encode categorical features
    le_dict = {}
    df_encoded = df.copy()
    for column in df_encoded.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df_encoded[column] = le.fit_transform(df_encoded[column])
        le_dict[column] = le  # Save the LabelEncoder for each categorical column

    # Ensure the model directory exists
    os.makedirs('model', exist_ok=True)
    
    # Save the LabelEncoders
    joblib.dump(le_dict, 'model/label_encoders.pkl')

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
    Evaluate the performance of the trained RandomForest model on the test dataset.
    
    The function performs the following steps:
    1. Checks if the model file exists and loads it.
    2. Loads the LabelEncoder and applies it to encode categorical features.
    3. Loads the test dataset from a CSV file.
    4. Splits the data into features and target variables.
    5. Predicts the target values using the loaded model.
    6. Evaluates the model's performance using confusion matrix and classification report.
    """
    model_path = 'model/databreaches_model.pkl'
    le_path = 'model/label_encoders.pkl'
    
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

    report = classification_report(y_true, y_pred, zero_division=0)
    print("Databreaches Data Classification Report:\n", report)

def main():
    """
    Execute the training and evaluation of the RandomForest model.
    
    The function calls:
    - `train_and_save_model()`: To train and save the model.
    - `evaluate_databreaches_model()`: To evaluate the saved model's performance.
    """
    train_and_save_model()
    evaluate_databreaches_model()

if __name__ == "__main__":
    main()









