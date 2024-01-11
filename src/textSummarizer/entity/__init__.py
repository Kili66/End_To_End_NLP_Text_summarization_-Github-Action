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