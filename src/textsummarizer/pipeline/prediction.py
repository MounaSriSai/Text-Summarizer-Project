from textsummarizer.config.configuration import ConfigurationManager
from transformers import pipeline
from transformers import AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
    def predict(self, text):
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

            # Get the model's max length (typically 1024 for Pegasus)
            max_input_length = tokenizer.model_max_length if tokenizer.model_max_length != float('inf') else 1024

            # Tokenize the input text
            tokens = tokenizer.encode(text, truncation=False, add_special_tokens=True)

            # Truncate if necessary (leave some buffer for generation)
            if len(tokens) > max_input_length - 50:  # Buffer for safety
                tokens = tokens[:max_input_length - 50]
                text = tokenizer.decode(tokens, skip_special_tokens=True)

            pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
            print("Dialogue:")
            print(text)

            output = pipe(text, **gen_kwargs)[0]['summary_text']
            print("Summary:")
            print(output)
            return output
        except Exception as e:
            print(f"Error during summarization: {str(e)}")
            return f"An error occurred while summarizing the text: {str(e)}"
