import pandas as pd
from sensor.logger import logging 
from sensor.exception import SensorException
from sensor.config import mongo_client

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:

    """
    This fucntion returns collection as dataframe
    params:
    database_name: database name 
    collection_name: collection name
    ===========================
    returns pandas dataframe of a collection
    """

    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id", axis = 1)
        logging.info(f"row and columnns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)
