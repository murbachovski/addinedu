# https://huggingface.co/black-forest-labs/FLUX.1-dev

from huggingface_hub import InferenceClient
import os

os.environ["HF_TOKEN"] = ""

client = InferenceClient(
    provider="auto",
    api_key=os.environ["HF_TOKEN"]
)
answer = input("이미지로 생성할 문장을 입력하세요: ")

# output is a PIL.Image object
image = client.text_to_image(
    answer,
    model="black-forest-labs/FLUX.1-dev",
)

# 저장 또는 표시
image.save("output_image.png")  # 이미지 파일로 저장

print("SUCCESS")