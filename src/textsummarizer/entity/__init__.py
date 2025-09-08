from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    s3_bucket_name: str
    input_key: str
    output_key: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    all_required_files: list
    
@dataclass(frozen=True)
class DataTransformerConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path