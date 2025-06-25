from transformers import pipeline

# 감정분석 파이프라인 생성
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentences = [
    "I don't like a bird.",
    "I like a bird."
]

for s in sentences:
    result = sentiment_analyzer(s)[0]
    print(f"문장: {s}")
    print(f"감정: {result['label']}, 점수: {result['score']:.4f}")
    print()
