import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    plt.close()  # Close plot to avoid displaying it

    # Metrics - Placeholder for future visualizations
    # plt.figure(figsize=(10, 6))
    # sns.some_metric_plot(...)
    # plt.title('Metric Visualization')
    # plt.xlabel('Metric')
    # plt.ylabel('Value')
    # plt.savefig('vis/metrics_visualization.png')
    # plt.close()

    # Outputs - Placeholder for final output visualizations
    # plt.figure(figsize=(10, 6))
    # sns.some_output_plot(...)
    # plt.title('Output Visualization')
    # plt.xlabel('Output')
    # plt.ylabel('Value')
    # plt.savefig('vis/outputs_visualization.png')
    # plt.close()

    # Model Evaluation - Placeholder for model evaluation visualizations
    # plt.figure(figsize=(10, 6))
    # sns.some_model_evaluation_plot(...)
    # plt.title('Model Evaluation')
    # plt.xlabel('Evaluation Metric')
    # plt.ylabel('Value')
    # plt.savefig('vis/model_evaluation.png')
    # plt.close()

    # Non-Technical Audience - Placeholder for simplified visualizations
    # plt.figure(figsize=(10, 6))
    # sns.some_simplified_plot(...)
    # plt.title('Non-Technical Audience Visualization')
    # plt.xlabel('Aspect')
    # plt.ylabel('Value')
    # plt.savefig('vis/non_technical_audience.png')
    # plt.close()

if __name__ == "__main__":
    visualize_data()

