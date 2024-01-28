from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger
import os

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        # Use the same model_path, tokenizer_path, and data_path arguments as in the model trainer code
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config, model_path=os.path.join(self.config.root_dir,"pegasus-samsum-model"), tokenizer_path=os.path.join(self.config.root_dir,"tokenizer"), data_path=self.config.data_path)
        model_evaluation_config.evaluate()
