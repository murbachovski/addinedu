# pip install -U transformers
# pip install torch
# huggingface의 고속 다운로드 기능(xet)을 활성화하려면 hf_xet 설치가 필요하다는 의미
# pip install huggingface_hub[hf_xet]

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

