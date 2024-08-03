import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
    # Load the processed data
    df = pd.read_csv('/System/Volumes/Data/Users/diyasayal/Desktop/INST414/databreaches.csv')

    # Example 1: Distribution of Records
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Records'], kde=True)
    plt.title('Distribution of Records')
    plt.xlabel('Number of Records')
    plt.ylabel('Frequency')
    plt.savefig('vis/distribution_of_records.png')
    plt.show()

    # Example 2: Count of Breaches by Method
    plt.figure(figsize=(12, 8))
    sns.countplot(x='Method', data=df)
    plt.title('Count of Breaches by Method')
    plt.xlabel('Breach Method')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.savefig('vis/count_by_method.png')
    plt.show()

if __name__ == "__main__":
    visualize_data()