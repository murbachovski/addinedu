# https://huggingface.co/openai/clip-vit-large-patch14
# https://huggingface.co/docs/transformers/main/en/model_doc/clip#clip

# python3.10
# pip install transformers
# pip install torch
# pip install pillow
# pip install matplotlib

# Use a pipeline as a high-level helper
from transformers import pipeline
from PIL import Image
import requests
import matplotlib.pyplot as plt
from transformers import CLIPProcessor, CLIPModel

pipe = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

# 모델과 프로세서 불러오기 (use_fast=True 옵션 추가)
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 이미지 로드
url = "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# 텍스트 라벨도 바꿔보기
texts = ["hamburger", "pizza", "salad", "dog", "bus", "cat", "car", "bicycle", "train", "airplane"]

# 전처리
inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

# 추론
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

# 이미지 출력
plt.imshow(image)
plt.axis('off')
plt.show()

# 결과 출력
for text, prob in zip(texts, probs[0]):
    print(f"{text}: {prob.item()*100:.2f}%")