from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from starlette.middleware.cors import CORSMiddleware
import torch

# Load model & tokenizer từ thư mục local
model_path = "./best_model"
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForQuestionAnswering.from_pretrained(model_path, local_files_only=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Cấu hình CORS (cho phép truy cập từ tất cả các origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Khai báo schema đầu vào
class QARequest(BaseModel):
    question: str
    context: str

# Hàm đọc hiểu nâng cao
def answer_question_advanced(question, context):
    inputs = tokenizer(
        question,
        context,
        return_tensors="pt",
        truncation="only_second",
        max_length=384,
        stride=128,
        padding="max_length",
        return_overflowing_tokens=True,
        return_offsets_mapping=True
    ).to(device)

    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    offset_mapping = inputs["offset_mapping"]
    overflow_to_sample_mapping = inputs["overflow_to_sample_mapping"]

    best_score = -float("inf")
    best_answer = ""

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

    for i in range(len(input_ids)):
        start_logit = start_logits[i]
        end_logit = end_logits[i]

        start_idx = torch.argmax(start_logit)
        end_idx = torch.argmax(end_logit)

        if start_idx > end_idx:
            continue

        score = start_logit[start_idx] + end_logit[end_idx]
        if score > best_score:
            best_score = score
            offsets = offset_mapping[i]

            start_char = offsets[start_idx][0]
            end_char = offsets[end_idx][1]

            if start_char is None or end_char is None:
                continue

            best_answer = context[start_char:end_char]

    return best_answer.strip() if best_answer.strip() else "🤔 Không tìm thấy câu trả lời phù hợp."

# Endpoint chính
@app.post("/qa")
def answer_question(req: QARequest):
    print(f"Question: {req.question}")
    print(f"Context: {req.context}")
    answer = answer_question_advanced(req.question, req.context)
    return {"answer": answer}
