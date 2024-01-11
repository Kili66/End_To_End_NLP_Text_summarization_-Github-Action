from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
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