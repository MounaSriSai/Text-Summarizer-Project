from textsummarizer.pipeline.data_ingestion_stage1 import DataIngestionPipeline
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