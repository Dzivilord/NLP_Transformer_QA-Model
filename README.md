# NLP_Transformer_QA-Model

## Description

## Getting started

### Prerequisites

- Python > 3.12.5

### Installation

Create and activate a virtual environment (optional but recommended)

```cmd
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install dependencies

```cmd
pip install -r requirements.txt
```

## Project Structure

```
NLP_Transformer_QA-Model
├── BE_AnswerAndQuestion/                         # Contains backend source code built with FastAPI
│   ├── app.py                                    # Main file that starts the FastAPI app, defines the API, and loads the model from best_model
│   ├── extract_data.ipynb                        # Jupyter notebook for initial data processing and extraction for training
│   ├── Medical_Question_Answering_*.ipynb        # Main notebook for training the question-answering (QA) model
│   ├── README.md                                 # Instructions on how to install and run the backend
│   └── best_model/                               # Directory containing the fine-tuned QA model for reading comprehension
│       └── ...                                   # Model files, configuration, and tokenizer files (e.g., config.json, model.bin)
├── FE_AnswerAndQuestion/                         # Contains frontend source code built with Vue.js
│   └── ...                                       # Includes folders like src/, public/, vite config, tsconfig, etc. (see frontend section for details)
├── dataset/                                      # Folder containing dataset-related information
│   └── Dataset_Link.txt                          # File with the download link or reference to the dataset used for training
├── docs/                                         # Documentation folder
│   └── Report.docx                               # Final report describing the development process and model results
├── .gitignore                                    # Specifies files/folders to be ignored by Git
├── README.md                                     # Project overview, including setup instructions, usage, and deployment guide
└── requirements.txt                              # List of Python dependencies required to run the backend
```
