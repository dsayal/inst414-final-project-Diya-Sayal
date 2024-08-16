import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_data():
    """
    Visualize the data breaches data with various plots.

    This function performs the following visualizations:
    1. EDA - Distribution of Records: A histogram with KDE to show the distribution of the 'Records' column.
    2. EDA - Count of Breaches by Method: A count plot to show the frequency of different breach methods.
    3. Metrics - Additional visualizations based on calculated metrics.
    4. Outputs - Visualizations for final outputs or insights.
    5. Model Evaluation - Visualizations for evaluating the model performance.
    6. Non-Technical Audience - Simplified visualizations for a broader audience.
    """
    # Load the processed data
    df = pd.read_csv('/System/Volumes/Data/Users/diyasayal/Desktop/INST414/databreaches.csv')

    # EDA - Distribution of Records
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Records'], kde=True)
    plt.title('Distribution of Records')
    plt.xlabel('Number of Records')
    plt.ylabel('Frequency')
    plt.savefig('vis/eda_distribution_of_records.png')  # Updated filename for EDA
    plt.close()  # Close plot to avoid displaying it

    # EDA - Count of Breaches by Method
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Method', data=df)
    plt.title('Count of Breaches by Method')
    plt.xlabel('Breach Method')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.savefig('vis/eda_count_by_method.png')  # Updated filename for EDA
    plt.close()

    # Define the corrected lengths
    class_list = list(range(68))
    precision_list = [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 1.00, 0.50, 0.00, 1.00, 1.00, 0.50, 1.00, 0.00, 1.00, 1.00, 0.50, 0.73, 1.00, 1.00, 1.00, 1.00, 0.73, 1.00, 0.71, 1.00, 0.50, 1.00, 1.00, 1.00, 1.00, 0.50, 0.75, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.69, 0.00, 1.00, 0.86, 1.00, 0.00, 1.00, 0.78, 0.00, 0.00, 0.00, 1.00, 0.67, 1.00, 0.75, 0.50, 0.71, 1.00, 0.00, 1.00]
    recall_list = [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.85, 1.00, 0.00, 1.00, 1.00, 1.00, 1.00, 0.00, 1.00, 0.75, 1.00, 0.63, 1.00, 1.00, 1.00, 1.00, 0.73, 1.00, 0.86, 1.00, 0.50, 1.00, 1.00, 1.00, 0.67, 1.00, 0.86, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.74, 0.00, 1.00, 0.75, 1.00, 0.00, 1.00, 0.74, 0.00, 0.00, 0.00, 1.00, 0.67, 1.00, 0.43, 1.00, 0.87, 1.00, 0.00, 1.00]
    f1_score_list = [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.92, 0.67, 0.00, 1.00, 1.00, 0.67, 1.00, 0.00, 1.00, 0.86, 0.67, 0.73, 1.00, 1.00, 1.00, 1.00, 0.73, 0.78, 0.76, 1.00, 0.50, 1.00, 1.00, 1.00, 0.80, 0.67, 0.80, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.71, 0.00, 1.00, 0.80, 1.00, 0.00, 1.00, 0.76, 0.00, 0.00, 0.00, 1.00, 0.80, 1.00, 0.55, 0.67, 0.78, 1.00, 0.00, 1.00]
    support_list = [1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 38, 1, 1, 1, 1, 11, 1, 29, 1, 2, 2, 1, 3, 1, 7, 1, 2, 1, 1, 1, 3, 27, 1, 2, 8, 1, 1, 19, 2, 1, 2, 1, 12, 1, 7, 1, 53, 1, 1]

    # Fill shorter lists with NaNs
    max_length = len(class_list)

    precision_list.extend([np.nan] * (max_length - len(precision_list)))
    recall_list.extend([np.nan] * (max_length - len(recall_list)))
    f1_score_list.extend([np.nan] * (max_length - len(f1_score_list)))
    support_list.extend([np.nan] * (max_length - len(support_list)))

    # Verify all lists are now of the same length
    assert len(precision_list) == len(class_list)
    assert len(recall_list) == len(class_list)
    assert len(f1_score_list) == len(class_list)
    assert len(support_list) == len(class_list)

    # Create DataFrame
    metrics_data = {
        'Class': class_list,
        'Precision': precision_list,
        'Recall': recall_list,
        'F1-Score': f1_score_list,
        'Support': support_list
    }

    metrics_df = pd.DataFrame(metrics_data)

    # Set up the figure and axes
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))

    # Plot Precision
    sns.barplot(x='Class', y='Precision', data=metrics_df, ax=axes[0], color='blue')
    axes[0].set_title('Precision per Class')
    axes[0].set_xlabel('Class')
    axes[0].set_ylabel('Precision')

    # Plot Recall
    sns.barplot(x='Class', y='Recall', data=metrics_df, ax=axes[1], color='green')
    axes[1].set_title('Recall per Class')
    axes[1].set_xlabel('Class')
    axes[1].set_ylabel('Recall')

    # Plot F1-Score
    sns.barplot(x='Class', y='F1-Score', data=metrics_df, ax=axes[2], color='red')
    axes[2].set_title('F1-Score per Class')
    axes[2].set_xlabel('Class')
    axes[2].set_ylabel('F1-Score')

    plt.tight_layout()
    plt.savefig('vis/metrics_visualization.png')  # Save all metrics plots in one file
    plt.close()

if __name__ == "__main__":
    visualize_data()



