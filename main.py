from textsummarizer.pipeline.data_ingestion_stage1 import DataIngestionPipeline
from textsummarizer.pipeline.data_validation_stage2 import DataValidationTrainingPipeline
from textsummarizer.pipeline.data_transformation_stage3 import DataTransformationTrainingPipeline
from textsummarizer.pipeline.model_training_stage4 import ModelTrainingPipeline
from textsummarizer.pipeline.model_evaluation_stage5 import ModelEvaluationPipeline
from textsummarizer.logging import logger

Stage_name = 'Data Ingestion Stage'
try:
    logger.info(f">>>>> stage{Stage_name} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {Stage_name} completed <<<<<<\n\nx=======")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = 'Data Validation Stage'
try:
    logger.info(f">>>>> stage{Stage_name} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {Stage_name} completed <<<<<<\n\nx=======")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = 'Data Transformation Stage'
try:
    logger.info(f">>>>> stage{Stage_name} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Stage {Stage_name} completed <<<<<<\n\nx=======")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = 'Model Training Stage'
try:
    logger.info(f">>>>> stage{Stage_name} started <<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> Stage {Stage_name} completed <<<<<<\n\nx=======")
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = 'Model Evaluation Stage'
try:
    logger.info(f">>>>> stage{Stage_name} started <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.run()
    logger.info(f">>>>>> Stage {Stage_name} completed <<<<<<\n\nx=======")
except Exception as e:
    logger.exception(e)
    raise e
