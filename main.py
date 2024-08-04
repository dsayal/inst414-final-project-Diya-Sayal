from etl.extract import extract_databreaches_data, extract_cyberbreaches_data
from etl.transform import transform_databreaches_data, transform_cyberbreaches_data
from analysis.model import train_and_save_model, evaluate_databreaches_model
from etl.load import load_databreaches_data, load_cyberbreaches_data
from vis.visualize import visualize_data

def main():
    """
    Main function to run the data pipeline steps in sequence:
    1. Extract Data
    2. Transform Data
    3. Train and Save Model
    4. Evaluate Model
    5. Visualize Data
    """
    # Step 1: Extract Data
    print("Extracting data...")
    extract_databreaches_data()
    extract_cyberbreaches_data()

    # Step 2: Transform Data
    print("Transforming data...")
    transform_databreaches_data()
    transform_cyberbreaches_data()

    # Step 3: Train and Save Model
    print("Training and saving model...")
    train_and_save_model()

    # Step 4: Evaluate Model
    print("Evaluating model...")
    evaluate_databreaches_model()

    # Step 5: Visualize Data
    print("Visualizing data...")
    visualize_data()

if __name__ == "__main__":
    main()


