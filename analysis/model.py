import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_graphviz
import joblib
import os
import pydotplus
from graphviz import Source
from io import StringIO

def train_and_save_model():
    """
    Train a RandomForest model using the processed breach data and save it to a file.
    
    The function performs the following steps:
    1. Loads the transformed dataset from a CSV file.
    2. Encodes categorical features to numeric values using LabelEncoder.
    3. Splits the data into training and testing sets.
    4. Initializes and trains a RandomForestClassifier model.
    5. Saves the trained model and LabelEncoder to files.
    6. Visualizes the first decision tree in the RandomForest and saves it as a PNG file.
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

    # Ensure the model and outputs directories exist
    os.makedirs('outputs/model', exist_ok=True)
    
    # Save the LabelEncoders
    joblib.dump(le_dict, 'outputs/model/label_encoders.pkl')

    # Split data
    X = df_encoded.drop(columns=['Organization type'])
    y = df_encoded['Organization type']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'outputs/model/databreaches_model.pkl')

    # Visualize the first decision tree in the RandomForest
    # Extract one of the decision trees from the RandomForest
    estimator = model.estimators_[0]
    dot_data = StringIO()
    export_graphviz(estimator, out_file=dot_data, feature_names=X.columns, 
                    class_names=model.classes_, filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    
    # Save the decision tree as a PNG file
    png_path = 'outputs/model/decision_tree.png'
    graph.write_png(png_path)
    print(f"Decision tree saved to {png_path}")








