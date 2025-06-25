# 문맥적 의미 유사도
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
emb1 = model.encode("There is family with dog he is so nice", convert_to_tensor=True)
emb2 = model.encode("Wow, fantastic. How did you to that?", convert_to_tensor=True)

cos_sim = util.pytorch_cos_sim(emb1, emb2)
print(f"유사도: {cos_sim.item():.4f}")
