# pip install pytesseract
# pip install pillow

import pytesseract # 이미지에서 글자를 읽어내는 OCR 라이브러리
from PIL import Image # 이미지를 읽기 위한 도구

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = Image.open("v09_ocr/testocr.png")

results = pytesseract.image_to_string(image, lang='kor')

print(results)