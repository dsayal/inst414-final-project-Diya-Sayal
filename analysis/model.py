import pandas as pd

def train_and_save_model():
    # Update the path to the dataset
    df = pd.read_csv('/Users/diyasayal/Desktop/INST414/databreaches.csv')
    
    # Print the column names to check the actual names
    print("Columns in the DataFrame:", df.columns)
    
    # Proceed with the rest of your code
    X = df.drop('Type_Of_Breach', axis=1)  # Feature columns
    y = df['Type_Of_Breach']               # Target column

    # Convert categorical variables to numerical if necessary
    X = pd.get_dummies(X)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the Decision Tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, 'model/databreaches_model.pkl')
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_and_save_model()

