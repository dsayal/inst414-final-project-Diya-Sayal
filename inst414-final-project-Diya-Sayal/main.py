from etl.extract import extract_data
from etl.transform import load_extracted_data, clean_data
from analysis.model import train_model
from vis.visualizations import create_visualizations

def main():
    # Extract
    file_path = 'data/raw/Cyber Security Breaches.csv'
    data = extract_data(file_path)
    data.to_csv('data/extracted/cyber_security_breaches.csv', index=False)
    
    # Transform and load
    data = load_extracted_data('data/extracted/cyber_security_breaches.csv')
    cleaned_data = clean_data(data)
    cleaned_data.to_csv('data/processed/cleaned_cyber_security_breaches.csv', index=False)
    
    # Analyze
    model, accuracy = train_model(cleaned_data)
    print(f'Model Accuracy: {accuracy}')
    
    # Visualize
    create_visualizations(cleaned_data)

if __name__ == '__main__':
    main()