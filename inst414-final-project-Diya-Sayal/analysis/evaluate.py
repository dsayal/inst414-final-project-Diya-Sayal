import pandas as pd
from sklearn.metrics import confusion_matrix, roc_auc_score

def evaluate_databreaches_model():
    """
    Evaluate additional metrics for databreaches data.
    """
    df = pd.read_csv('data/processed/databreaches_data_transformed.csv')
    y_true = df['target_column']  # Replace with actual target variable
    y_pred = df['predicted_column']  # Replace with actual predicted column

    # Confusion matrix
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Databreaches Data Confusion Matrix:\n", conf_matrix)

    # ROC AUC score
    roc_auc = roc_auc_score(y_true, y_pred)
    print("Databreaches Data ROC AUC Score:", roc_auc)

def evaluate_cyberbreaches_model():
    """
    Evaluate additional metrics for cyberbreaches data.
    """
    df = pd.read_csv('data/processed/cyberbreaches_data_transformed.csv')
    y_true = df['target_column']  # Replace with actual target variable
    y_pred = df['predicted_column']  # Replace with actual predicted column

    # Confusion matrix
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Cyberbreaches Data Confusion Matrix:\n", conf_matrix)

    # ROC AUC score
    roc_auc = roc_auc_score(y_true, y_pred)
    print("Cyberbreaches Data ROC AUC Score:", roc_auc)

def main():
    evaluate_databreaches_model()
    evaluate_cyberbreaches_model()

if __name__ == "__main__":
    main()
