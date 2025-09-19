# Text Summarizer Project

Welcome to the Text Summarizer Project, a Python application designed for natural language processing tasks. This project leverages machine learning models to provide efficient text summarization capabilities, integrated with a FastAPI-based web API for seamless access.

## Features

- Automated text summarization using state-of-the-art transformer models
- RESTful API built with FastAPI for easy integration
- Configurable parameters to customize model behavior

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Mouna/Text-Summarizer-Project.git
   cd Text-Summarizer-Project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the API

Start the FastAPI server with the following command:
```
python app.py
```

The API will be accessible at `http://localhost:8080`.

### API Endpoints

- `GET /docs`: Interactive API documentation (Swagger UI)
- `GET /predict?text=<your_text>`: Obtain a summary of the input text

### Model Training

To train the summarization model:
```
python main.py
```

## Repository

Explore the full project on GitHub: [https://github.com/Mouna/Text-Summarizer-Project]
