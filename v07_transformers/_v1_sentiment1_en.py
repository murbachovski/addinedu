# 텍스트 감정 분석
# pip install transformers datasets
# pip install torch

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

### ENG ###

# 단수 입력
results = classifier("I'm so happy")
print(results)

# 복수 입력
# results = classifier(["I love you", "I kill you"])
# for result in results:
#     print(f"label: {result['label']}, with score: {round(result['score'], 3)}")