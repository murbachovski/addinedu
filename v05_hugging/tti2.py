# Python==3.9.21
# pip install diffusers
# pip install torch X
# pip install transformers
# pip install accelerate
# 실행됨

from diffusers import StableDiffusionPipeline
# import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    # torch_dtype=torch.float16
    )
pipe = pipe.to("cpu")  # or "mps" for Mac M1/M2

prompt = "horse"
image = pipe(prompt).images[0]
image.save("./output.png")
print("SUCCESS")