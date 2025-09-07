from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_ingestion import DataIngestion
from textsummarizer.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

# Load dataset from S3
        dataset = data_ingestion.load_dataset_from_s3()

# Save locally
        data_ingestion.save_local(dataset)