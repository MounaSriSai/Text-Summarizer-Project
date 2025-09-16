import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(os.path.join(os.getcwd(), "src"))

from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.pipeline.model_evaluation_stage5 import ModelEvaluationPipeline

def test_wrong_model_path():
    """Test with wrong model path"""
    print("Testing with wrong model path...")
    try:
        config_manager = ConfigurationManager()
        config = config_manager.get_model_evaluation_config()
        # Change to wrong path
        config.model_path = Path("artifacts/wrong_model")
        pipeline = ModelEvaluationPipeline(config)
        pipeline.main()
        print("ERROR: Should have failed")
    except Exception as e:
        print(f"Expected error: {e}")

def test_wrong_tokenizer_path():
    """Test with wrong tokenizer path"""
    print("Testing with wrong tokenizer path...")
    try:
        config_manager = ConfigurationManager()
        config = config_manager.get_model_evaluation_config()
        config.tokenizer_path = Path("artifacts/wrong_tokenizer")
        pipeline = ModelEvaluationPipeline(config)
        pipeline.main()
        print("ERROR: Should have failed")
    except Exception as e:
        print(f"Expected error: {e}")

def test_wrong_data_path():
    """Test with wrong data path"""
    print("Testing with wrong data path...")
    try:
        config_manager = ConfigurationManager()
        config = config_manager.get_model_evaluation_config()
        # dataclasses are frozen, so create new config with wrong data path
        from dataclasses import replace
        config = replace(config, data_path=Path("artifacts/wrong_data"))
        pipeline = ModelEvaluationPipeline(config)
        pipeline.main()
        print("ERROR: Should have failed")
    except Exception as e:
        print(f"Expected error: {e}")

if __name__ == "__main__":
    test_wrong_model_path()
    test_wrong_tokenizer_path()
    test_wrong_data_path()
    print("Error handling tests completed.")
