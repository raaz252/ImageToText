import pathlib
import pytesseract
from PIL import Image

BASE_DIR=pathlib.Path(__file__).parent
print(BASE_DIR)
IMG_DIR=BASE_DIR/"images"
img_path=IMG_DIR/"Screenshot (20).png"

img=Image.open(img_path)
preds=pytesseract.image_to_string(img)
print(preds)