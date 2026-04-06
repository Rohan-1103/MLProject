import os
import sys
from src.mlprojet.exception import CustomException
from src.mlprojet.logger import logging
import pandas as pd
from src.mlprojet.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# dataclass
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            ## Reading data from mysql
            df = pd.read_csv(os.path.join('notebook/data', 'raw.csv'))
            logging.info("Reading from MySql database completed")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # raw data saving
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            train_set, test_set=train_test_split(df, test_size=0.20, random_state=42)
            # train data saving
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # test data saving
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data Ingestion completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
            
        

    
    