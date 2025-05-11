# NLP_Transformer_QA-Model

## Description

In the healthcare field, prescriptions often contain specialized terminology, lengthy, and complex content. This makes it difficult for patients to understand the information on the prescription, and even doctors may waste time when looking up or summarizing the details quickly. Therefore, building an automatic Question Answering (QA) model that can extract information from prescriptions accurately and promptly based on user queries would greatly improve time efficiency, communication effectiveness, and ensure treatment accuracy.

In this project, we leverage pre-trained models for inference and fine-tune them on prescription-related datasets. By fine-tuning models such as BERT, RoBERTa, and it's variants, we aim to enhance the model’s ability to understand and extract medical-specific information. The fine-tuned model will then be capable of answering user queries with higher precision, making it a powerful tool for both patients and healthcare professionals.

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
<<<<<<< HEAD
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
=======
<GroupID>
├── F1
│   ├── F11
│   │   ├── File 1
│   │   ├── File 2
│   │   └── ...
│   ├── F11
│   │   ├── File 1
│   │   ├── File 2
│   │   └── ...
│   ├── F11
│   │   ├── File 1
│   │   ├── File 2
├── docs
│   └── Report.pdf
├── requiremnts.txt
├── README
>>>>>>> 8465b7af367b54de9de4cdcb9d244b971a880bac
```
