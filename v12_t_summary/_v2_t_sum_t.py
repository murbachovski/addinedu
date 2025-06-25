# BERT 기반 T5 모델과 한국어 번역 라이브러리 
# pip install -U transformers
# pip install torch
# huggingface의 고속 다운로드 기능(xet)을 활성화하려면 hf_xet 설치가 필요하다는 의미
    # pip install huggingface_hub[hf_xet]
# 번역
    # https://www.youtube.com/watch?v=k29lfExfExQ
    # pip install googletrans==4.0.0-rc1

# Use a pipeline as a high-level helper
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

summary = summarizer(
'''
The Alchemist (Portuguese: O Alquimista) is a novel by Brazilian author Paulo Coelho which was first published in 1988. Originally written in Portuguese, it became a widely translated international bestseller. The story follows the shepherd boy Santiago in his journey across North Africa to the Egyptian pyramids after he dreams of finding treasure there.
'''   
)

sum = summary[0]['summary_text']

print(f" #### SUM : {sum} #### ")

from googletrans import Translator

def translate_text(text):
    """
    주어진 텍스트를 한국어로 번역하는 함수
    """
    translator = Translator()
    translation = translator.translate(text, dest='ko')
    translated_text = translation.text
    
    return translated_text

translated = translate_text(sum)

print(f" #### translate : {translated} #### ")