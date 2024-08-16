import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import graphviz

def train_and_save_model():
    """
    Train a Decision Tree model and save it to a file.
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

    # Initialize and train Decision Tree model
    model = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'model/databreaches_model.pkl')

    # Visualize the tree as text
    tree_text = export_text(model, feature_names=list(X_train.columns))
    print("Decision Tree as Text:\n", tree_text)

    # Visualize the tree as a graph
    dot_data = export_graphviz(model, out_file=None,
                               feature_names=list(X_train.columns),
                               class_names=[str(cls) for cls in le.classes_],
                               filled=True, rounded=True,
                               special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render("model/decision_tree")  # This will save the tree as a PDF file

def evaluate_databreaches_model():
    """
    Evaluate metrics for the databreaches data using Decision Tree model.
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







