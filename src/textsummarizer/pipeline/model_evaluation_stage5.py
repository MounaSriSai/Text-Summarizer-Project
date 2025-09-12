import os
from pathlib import Path
from textsummarizer.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import evaluate
import pandas as pd
import torch
from textsummarizer.logging import logger
from tqdm import tqdm

class ModelEvaluationPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.config = self.config_manager.get_model_evaluation_config()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        """Yield successive n-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i + batch_size]

    def calculate_metrics(self, dataset, metric, model, tokenizer, batch_size=16,
                          column_text='dialogue', column_summary='summary'):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(zip(article_batches, target_batches), total=len(article_batches)):
            inputs = tokenizer(article_batch, max_length=1024, truncation=True,
                               padding="max_length", return_tensors="pt")

            summaries = model.generate(input_ids=inputs["input_ids"].to(self.device),
                                       attention_mask=inputs["attention_mask"].to(self.device),
                                       length_penalty=0.8, num_beams=8, max_length=128)

            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,
                                                  clean_up_tokenization_spaces=True)
                                 for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries, references=target_batch)

        score = metric.compute()
        return score

    def run(self):
        logger.info("Starting model evaluation pipeline")
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(self.device)

        dataset = load_from_disk(self.config.data_path)
        logger.info(f"Loaded dataset from {self.config.data_path}")

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = evaluate.load('rouge')

        # Evaluate on full test set or configurable subset
        test_dataset = dataset['test']
        logger.info(f"Evaluating on test dataset with {len(test_dataset)} samples")

        score = self.calculate_metrics(test_dataset, rouge_metric, model, tokenizer,
                                       batch_size=16, column_text='dialogue', column_summary='summary')

        rouge_dict = {rn: score[rn].mid.fmeasure for rn in rouge_names}
        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        metric_file_path = Path(self.config.metric_file_name)
        metric_file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(metric_file_path, index=False)
        logger.info(f"Saved evaluation metrics to {metric_file_path}")

        logger.info("Model evaluation pipeline completed successfully")

if __name__ == "__main__":
    pipeline = ModelEvaluationPipeline()
    pipeline.run()
