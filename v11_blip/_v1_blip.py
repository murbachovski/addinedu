# python 3.11.13
# pip install -U transformers
# pip install pillow
# pip install torch
# Use a pipeline as a high-level helper
# https://huggingface.co/Salesforce/blip-image-captioning-large

from transformers import pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import warnings
warnings.filterwarnings(action='ignore')
from transformers import logging
logging.set_verbosity_error()  # 또는 set_verbosity_warning()도 가능

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# 이미지 로드
img_path = "v99_clip/hippo.jpg"
image = Image.open(img_path).convert("RGB")

# 모델 로드
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 텍스트 생성
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)

# print(processor.decode(out[0], skip_special_tokens=True))
caption = processor.decode(out[0], skip_special_tokens=True)

print("#########################")
print(f"자동 캡션 생성 : {caption}")
print("#########################")
