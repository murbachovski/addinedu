# pip install pymupdf

import pytesseract
from PIL import Image
import fitz

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Tesseract 설치 경로

doc = fitz.open('_resource/ocr.pdf')
page = doc.load_page(1)
mat = fitz.Matrix(3, 3)
pix = page.get_pixmap(matrix=mat)
output = "_resource/ocr.png"
pix.save(output)

# image = Image.open("_resource/ocr.jpg")
image = Image.open("_resource/ocr.png")
# results = pytesseract.image_to_string(image, lang='kor')
results = pytesseract.image_to_string(image)

print(results)
# print(results.split('\n')) 