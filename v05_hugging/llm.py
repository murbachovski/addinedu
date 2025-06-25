# https://huggingface.co/deepseek-ai/DeepSeek-R1-0528

import os
from huggingface_hub import InferenceClient

# 실습 보안상 비추천
os.environ["HF_TOKEN"] = ""

client = InferenceClient(
    provider="together",
    api_key=os.environ["HF_TOKEN"],
)

answer = input("질문을 입력해주세요. : ")

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-0528",
    messages=[
        {
            "role": "user",
            "content": answer
        }
    ],
)

print("==============================================")
print(completion.choices[0].message)
print("==============================================")