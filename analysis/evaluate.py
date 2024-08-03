from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
def evaluate_databreaches_model():
    """
    Evaluate additional metrics for databreaches data.
    """
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    y_true = df['Organization type']  # Actual labels
    y_pred = df['Method']  # Predicted labels

    # Accuracy
    accuracy = accuracy_score(y_true, y_pred)
    print("Databreaches Data Accuracy:", accuracy)

    # Classification report
    report = classification_report(y_true, y_pred)
    print("Databreaches Data Classification Report:\n", report)

def evaluate_cyberbreaches_model():
    """
    Evaluate additional metrics for cyberbreaches data.
    """
    df = pd.read_csv('data/processed/cyberbreaches_data_transformed.csv')
    y_true = df['Summary']  # Actual labels
    y_pred = df['Type_Of_Breach']  # Predicted labels

    # Accuracy
    accuracy = accuracy_score(y_true, y_pred)
    print("Cyberbreaches Data Accuracy:", accuracy)

    # Classification report
    report = classification_report(y_true, y_pred)
    print("Cyberbreaches Data Classification Report:\n", report)

def main():
    evaluate_databreaches_model()
    evaluate_cyberbreaches_model()

if __name__ == "__main__":
    main()

