from src.mlprojet.logger import logging
from src.mlprojet.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        a = 11 / 0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)