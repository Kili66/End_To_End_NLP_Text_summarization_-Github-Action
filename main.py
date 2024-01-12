from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline

from textSummarizer.logging import logger

STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f">>>>> {STAGE_NAME} Started >>>>")
    data_ingestion= DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>\n\n\n=======")
except Exception as e:
    logger.exception(e)
    raise e
#--------Data Validation-
STAGE_NAME= "Data validation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} Started >>>>")
    data_validation= DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>\n\n\n=======")
except Exception as e:
    logger.exception(e)
    raise e