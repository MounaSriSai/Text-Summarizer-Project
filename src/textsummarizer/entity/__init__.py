from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    s3_bucket_name: str
    input_key: str
    output_key: str
    local_data_file: Path
