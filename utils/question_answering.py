# utils/question_answering.py
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch

# Load BLIP model and processor for VQA
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def answer_question(image_path, question):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, question, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    answer = processor.decode(out[0], skip_special_tokens=True)
    return answer
