from src.mlprojet.components import data_ingestion
from src.mlprojet.logger import logging
from src.mlprojet.exception import CustomException
from src.mlprojet.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlprojet.components.data_transformation import DataTransformationConfig, DataTransformation
from src.mlprojet.components.model_trainer import ModelTrainerConfig, ModelTrainer

import sys
 
if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transormation(train_data_path, test_data_path)
        
        # model training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
        logging.info(f"Saved preprocessor at: {preprocessor_path}")
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)