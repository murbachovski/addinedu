# https://github.com/UB-Mannheim/tesseract/wiki
# pip install pytesseract
# pip install pillow

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Tesseract 설치 경로

image = Image.open("_resource/ocr.jpg")
results = pytesseract.image_to_string(image, lang='kor')

print(results)
