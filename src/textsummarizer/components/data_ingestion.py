import os
from pathlib import Path
from datasets import load_dataset
from textsummarizer.logging import logger
from textsummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def load_dataset_from_s3(self):
        """
        Load Hugging Face dataset directly from S3
        """
        dataset = load_dataset(
            "arrow",
            data_files={
                "train": f"s3://{self.config.s3_bucket_name}/samsum_dataset/train/data-00000-of-00001.arrow",
                "validation": f"s3://{self.config.s3_bucket_name}/samsum_dataset/validation/data-00000-of-00001.arrow",
                "test": f"s3://{self.config.s3_bucket_name}/samsum_dataset/test/data-00000-of-00001.arrow"
            }
        )
        logger.info(f"Dataset loaded with splits: {dataset.keys()}")
        return dataset

    def save_local(self, dataset):
        """
        Save dataset locally in Arrow format (keeps splits)
        """
        local_dir = Path(self.config.root_dir)
        local_dir.mkdir(parents=True, exist_ok=True)
        dataset.save_to_disk(str(local_dir))
        logger.info(f"Dataset saved locally at {local_dir}")
