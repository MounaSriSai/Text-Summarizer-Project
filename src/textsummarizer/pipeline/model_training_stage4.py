from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.model_trainer import ModelTrainer
from textsummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
