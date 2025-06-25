# 필요한 라이브러리 불러오기
from transformers import CLIPProcessor, CLIPModel  # HuggingFace에서 제공하는 CLIP 모델과 전처리기
from PIL import Image  # 이미지 파일 열기용
import torch  # 텐서 계산용
import matplotlib.pyplot as plt  # 이미지 시각화용

# 1. 사전 학습된 CLIP 모델과 전처리기 로딩
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")  # Vision + Text 인코더 모델
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")  # 텍스트+이미지 전처리기

# 2. 비교 대상 이미지들 (파일 경로 리스트)
image_paths = [
    "v99_clip/dog.jpg",
    "v99_clip/hippo.jpg",
    "v99_clip/owl.jpg",
    "v99_clip/tiger.jpg",
]
images = [Image.open(path).convert("RGB") for path in image_paths]  # 이미지 열고 RGB로 변환 (CLIP은 RGB 필요)

# 3. 유저로부터 자연어로 찾고 싶은 이미지 설명을 입력 받음
query = input("찾고 싶은 이미지 설명을 입력하세요: ")  # 예: "a cute dog"
# 일반적으로 "a photo of a {object}" 형태가 CLIP에 가장 잘 맞음
query = f"a photo of {query}"  # 자연어 스타일 보강

# 4. 텍스트와 여러 이미지 입력을 함께 전처리 (CLIP은 이 조합을 받아들일 수 있음)
inputs = processor(text=[query], images=images, return_tensors="pt", padding=True)  # 텐서로 변환

# 모델에 전처리된 입력을 넣고 추론 실행
outputs = model(**inputs)

# outputs.logits_per_image: 각 이미지와 텍스트 쌍에 대한 유사도 점수 (크면 유사)
# 이 점수들을 softmax로 확률화 → dim=0 기준 (여러 이미지 vs 1개 텍스트)
probs = outputs.logits_per_image.softmax(dim=0)

# 5. 각 이미지별로 예측된 텍스트와의 유사 확률 출력
print("각 이미지별 확률:")
for i, (path, prob) in enumerate(zip(image_paths, probs[:, 0])):  # 확률을 이미지별로 출력
    print(f"{i}: {path} -> {prob.item()*100:.2f}%")

# 확률이 가장 높은 이미지 인덱스 선택
best_idx = torch.argmax(probs[:, 0]).item()

# 해당 이미지를 출력하고 사용자에게 알려줌
print(f"\n🖼️ 가장 잘 어울리는 이미지: {image_paths[best_idx]}")
plt.imshow(images[best_idx])
plt.axis("off")  # 축 숨기기
plt.show()  # 이미지 시각화

