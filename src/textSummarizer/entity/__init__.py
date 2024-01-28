from dataclasses import dataclass
from pathlib import Path

# @decorator

@dataclass(frozen=True)
class DataIngestionConfig:
    #return variable types taken from config yaml file
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path