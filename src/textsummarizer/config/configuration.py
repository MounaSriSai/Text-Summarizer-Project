import sys
from textsummarizer.config_constants import *
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformerConfig, ModelTrainerConfig, ModelEvaluationConfig
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir=config.root_dir,
            s3_bucket_name=config.s3_bucket_name,
            input_key=config.input_key,
            output_key=config.output_key,
            local_data_file=config.local_data_file
        )
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config =DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_files=config.all_required_files,
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformerConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config =DataTransformerConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_name
        )
        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.Arguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=str(config.root_dir),
            data_path=str(config.data_path),
            model_checkpt=str(config.model_checkpt),
            num_train_epochs=params.num_train_epochs,
            per_device_train_batch_size=params.per_device_train_batch_size,
            warmup_steps=params.warmup_steps,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            eval_strategy=params.eval_strategy,
            eval_steps=int(params.eval_steps),
            save_steps=int(params.save_steps),
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name
        )
        return model_evaluation_config
