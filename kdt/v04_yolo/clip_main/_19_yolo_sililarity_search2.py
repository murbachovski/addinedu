from ultralytics import solutions

searcher = solutions.VisualAISearch(
    # data = "path/to/img/directory" # Optional, build search engine with your own images
    device="cpu"  # configure the device for processing i.e "cpu" or "cuda"
)

results = searcher("people studying")

# print(searcher.image_paths[0])
# Ranked Results:
#     - 000000546829.jpg | Similarity: 0.3269
#     - 000000549220.jpg | Similarity: 0.2899
#     - 000000517069.jpg | Similarity: 0.2761
#     - 000000029393.jpg | Similarity: 0.2742
#     - 000000534270.jpg | Similarity: 0.2680