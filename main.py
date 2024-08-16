import logging
from etl.extract import extract_databreaches_data, extract_cyberbreaches_data
from etl.transform import transform_databreaches_data, transform_cyberbreaches_data
from analysis.model import train_and_save_model, evaluate_databreaches_model
from etl.load import load_databreaches_data, load_cyberbreaches_data
from vis.visualize import visualize_data

# Configure logging
logging.basicConfig(filename='data_pipeline.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    """
    Main function to run the data pipeline steps in sequence:
    1. Extract Data
    2. Transform Data
    3. Train and Save Model
    4. Evaluate Model
    5. Visualize Data
    """
    logging.info("Starting data pipeline...")

    # Step 1: Extract Data
    try:
        logging.info("Extracting data...")
        extract_databreaches_data()
        extract_cyberbreaches_data()
    except Exception as e:
        logging.error(f"Error in data extraction: {e}")

    # Step 2: Transform Data
    try:
        logging.info("Transforming data...")
        transform_databreaches_data()
        transform_cyberbreaches_data()
    except Exception as e:
        logging.error(f"Error in data transformation: {e}")

    # Step 3: Train and Save Model
    try:
        logging.info("Training and saving model...")
        train_and_save_model()
    except Exception as e:
        logging.error(f"Error in model training and saving: {e}")

    # Step 4: Evaluate Model
    try:
        logging.info("Evaluating model...")
        evaluate_databreaches_model()
    except Exception as e:
        logging.error(f"Error in model evaluation: {e}")

    # Step 5: Visualize Data
    try:
        logging.info("Visualizing data...")
        visualize_data()
    except Exception as e:
        logging.error(f"Error in data visualization: {e}")

    logging.info("Data pipeline completed.")

if __name__ == "__main__":
    main()





