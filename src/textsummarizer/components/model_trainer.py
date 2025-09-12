from transformers import Trainer, TrainingArguments, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
from transformers import DataCollatorForSeq2Seq
from textsummarizer.entity import ModelTrainerConfig
from textsummarizer.logging import logger
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Starting model training")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {device}")

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_checkpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_checkpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        dataset_samsum = load_from_disk(self.config.data_path)
        logger.info(f"Dataset loaded from {self.config.data_path}")

        trainer_args = TrainingArguments(
            output_dir=str(self.config.root_dir),
            num_train_epochs=int(self.config.num_train_epochs),
            per_device_train_batch_size=int(self.config.per_device_train_batch_size),
            warmup_steps=int(self.config.warmup_steps),
            weight_decay=float(self.config.weight_decay),
            logging_steps=int(self.config.logging_steps),
            eval_strategy=str(self.config.eval_strategy),
            eval_steps=int(self.config.eval_steps),
            save_steps=int(self.config.save_steps),
            gradient_accumulation_steps=int(self.config.gradient_accumulation_steps)
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum["train"],
            eval_dataset=dataset_samsum["validation"]
        )

        trainer.train()
        logger.info("Training completed")

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
        logger.info("Model and tokenizer saved")
