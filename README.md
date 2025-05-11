# NLP_Transformer_QA-Model

## Description
In the healthcare field, prescriptions often contain specialized terminology, lengthy, and complex content. This makes it difficult for patients to understand the information on the prescription, and even doctors may waste time when looking up or summarizing the details quickly. Therefore, building an automatic Question Answering (QA) model that can extract information from prescriptions accurately and promptly based on user queries would greatly improve time efficiency, communication effectiveness, and ensure treatment accuracy.

In this project, we leverage pre-trained models for inference and fine-tune them on prescription-related datasets. By fine-tuning models such as BERT, RoBERTa, or T5, we aim to enhance the model’s ability to understand and extract medical-specific information. The fine-tuned model will then be capable of answering user queries with higher precision, making it a powerful tool for both patients and healthcare professionals.

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
```
 