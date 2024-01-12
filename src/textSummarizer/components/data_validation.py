import os
from textSummarizer.logging import logger
from pathlib import Path
from textSummarizer.entity import DataValidationConfig
# data val component , it will take configurations: data val configuration
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config= config
    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status= None
            
            all_files= os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status= False # in case files not found
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status {validation_status}")
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, "w") as f:
                      f.write(f"validation status {validation_status}")  
                                     
        except Exception as e:
            raise e