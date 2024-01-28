from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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

STAGE_NAME= "Data transformation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} Started >>>>")
    data_transformation= DataTransformationTrainPipeline()
    data_transformation.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>\n\n\n=======")
except Exception as e:
    logger.exception(e)
    raise e
### Model Trainer
STAGE_NAME= "Data Trainer stage"

try:
    logger.info(f">>>>> {STAGE_NAME} Started >>>>")
    model_trainer= ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>\n\n\n=======")
except Exception as e:
    logger.exception(e)
    raise e
## Model Evaluation
STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e