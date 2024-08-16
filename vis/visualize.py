import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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
    # File paths
    data_path = '/System/Volumes/Data/Users/diyasayal/Desktop/INST414/databreaches.csv'
    output_dir = 'vis'

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Load the processed data
        df = pd.read_csv(data_path)

        # EDA - Distribution of Records
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Records'], kde=True)
        plt.title('Distribution of Records')
        plt.xlabel('Number of Records')
        plt.ylabel('Frequency')
        plt.savefig(f'{output_dir}/eda_distribution_of_records.png')
        plt.close()

        # EDA - Count of Breaches by Method
        plt.figure(figsize=(12, 8))
        sns.countplot(x='Method', data=df)
        plt.title('Count of Breaches by Method')
        plt.xlabel('Breach Method')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.savefig(f'{output_dir}/eda_count_by_method.png')
        plt.close()

    except FileNotFoundError:
        print(f"Error: The file at {data_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create a DataFrame from the metrics
data = {
    'Class': list(range(68)),
    'Precision': [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 1.00, 0.50, 0.00, 1.00, 1.00, 0.50, 1.00, 0.00, 1.00, 1.00, 0.50, 0.73, 1.00, 1.00, 1.00, 1.00, 0.73, 1.00, 0.71, 1.00, 0.50, 1.00, 1.00, 1.00, 1.00, 0.50, 0.75, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.69, 0.00, 1.00, 0.86, 1.00, 0.00, 1.00, 0.78, 0.00, 0.00, 0.00, 1.00, 0.67, 1.00, 0.75, 0.50, 0.71, 1.00, 0.00, 1.00],
    'Recall': [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.85, 1.00, 0.00, 1.00, 1.00, 1.00, 1.00, 0.00, 1.00, 0.75, 1.00, 0.63, 1.00, 1.00, 1.00, 1.00, 0.73, 1.00, 0.86, 1.00, 0.50, 1.00, 1.00, 1.00, 0.67, 1.00, 0.86, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.74, 0.00, 1.00, 0.75, 1.00, 0.00, 1.00, 0.74, 0.00, 0.00, 0.00, 1.00, 0.67, 1.00, 0.43, 1.00, 0.87, 1.00, 0.00, 1.00],
    'F1-Score': [0.00, 1.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.92, 0.67, 0.00, 1.00, 1.00, 0.67, 1.00, 0.00, 1.00, 0.86, 0.67, 0.73, 1.00, 1.00, 1.00, 1.00, 0.73, 0.78, 0.76, 1.00, 0.50, 1.00, 1.00, 1.00, 0.80, 0.67, 0.80, 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 0.71, 0.00, 1.00, 0.80, 1.00, 0.00, 1.00, 0.76, 0.00, 0.00, 0.00, 1.00, 0.80, 1.00, 0.55, 0.67, 0.78, 1.00, 0.00, 1.00],
    'Support': [1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 38, 1, 1, 1, 1, 11, 1, 29, 1, 2, 2, 1, 3, 1, 7, 1, 2, 1, 1, 1, 3, 27, 1, 2, 8, 1, 1, 19, 2, 1, 2, 1, 12, 1, 7, 1, 53, 1, 1]
}

df = pd.DataFrame(data)

# Set up the figure and axes
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Plot Precision
sns.barplot(x='Class', y='Precision', data=df, ax=axes[0], palette='viridis')
axes[0].set_title('Precision per Class')
axes[0].set_xlabel('Class')
axes[0].set_ylabel('Precision')

# Plot Recall
sns.barplot(x='Class', y='Recall', data=df, ax=axes[1], palette='viridis')
axes[1].set_title('Recall per Class')
axes[1].set_xlabel('Class')
axes[1].set_ylabel('Recall')

# Plot F1-Score
sns.barplot(x='Class', y='F1-Score', data=df, ax=axes[2], palette='viridis')
axes[2].set_title('F1-Score per Class')
axes[2].set_xlabel('Class')
axes[2].set_ylabel('F1-Score')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('/Users/diyasayal/metrics_visualization.png')
plt.show()


if __name__ == "__main__":
    visualize_data()


