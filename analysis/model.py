import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

def train_and_save_model():
    # Load the dataset
    df = pd.read_csv('/Users/diyasayal/Desktop/INST414/databreaches.csv') 

    # Check for and handle missing values
    print("Missing values in the dataset:")
    print(df.isna().sum())
    
    # Handle missing values
    df = df.dropna()  # Dropping rows with missing values

    # Print columns for debugging
    print("Columns in the DataFrame:")
    print(df.columns)

    # Encode categorical features if necessary
    label_encoders = {}
    categorical_columns = ['Entity', 'Organization type', 'Method', 'Sources']
    for col in categorical_columns:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le

    # Select features and target
    X = df.drop('Method', axis=1, errors='ignore')  # Features
    y = df['Method']  # Target variable

    # Convert categorical features to numerical if needed
    X = pd.get_dummies(X) 

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'model/databreaches_model.pkl')

    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train_and_save_model()




