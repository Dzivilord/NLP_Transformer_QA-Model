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
├── BE_AnswerAndQuestion/                         # Thư mục chứa mã nguồn backend sử dụng FastAPI
│   ├── app.py                                    # File chính khởi chạy ứng dụng FastAPI, khai báo API, load mô hình từ best_model
│   ├── extract_data.ipynb                        # Notebook dùng để xử lý và trích xuất dữ liệu ban đầu cho huấn luyện
│   ├── Medical_Question_Answering_*.ipynb        # Notebook chính huấn luyện mô hình QA
│   ├── README.md                                 # Hướng dẫn cách cài đặt và chạy backend
│   └── best_model/                               # Thư mục chứa mô hình đã huấn luyện (fine-tuned) cho tác vụ đọc hiểu
│       └── ...                                   # Các file mô hình, config và tokenizer
├── FE_AnswerAndQuestion/                         # Thư mục chứa mã nguồn giao diện người dùng sử dụng Vue.js
│   └── ...                                       # Gồm các thư mục như src/, public/, cấu hình vite, tsconfig,... (xem chi tiết phần frontend)
├── dataset/                                      # Thư mục chứa thông tin về tập dữ liệu
│   └── Dataset_Link.txt                          # File chứa đường dẫn đến tập dữ liệu dùng để huấn luyện mô hình
├── docs/                                         # Thư mục lưu tài liệu báo cáo
│   └── Report.docx                               # Báo cáo mô tả toàn bộ quá trình phát triển và kết quả mô hình
├── .gitignore                                    # Định nghĩa các file/thư mục sẽ bị Git bỏ qua
├── README.md                                     # Tài liệu tổng quan mô tả dự án, cách sử dụng, cài đặt và triển khai
└── requirements.txt                              # Danh sách các thư viện Python cần thiết để chạy backend

```
