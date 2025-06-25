# 필요한 라이브러리 설치
# pip install transformers torch

from transformers import pipeline

# 감정분석 파이프라인 생성 (한국어 BERT 기반 모델)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="beomi/kcbert-base",
    tokenizer="beomi/kcbert-base"
)

# 테스트 문장
sentences = [
    "나는 오늘 기분이 좋아요.",
    "오늘은 정말 최악이에요.",
    "별로 마음에 들지 않아요.",
    "이 제품은 정말 최고예요!"
]

for s in sentences:
    result = sentiment_analyzer(s)[0]
    print(f"문장: {s}")
    print(f"감정: {result['label']}, 점수: {result['score']:.4f}\n")
