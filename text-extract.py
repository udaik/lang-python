import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("receipt.jpg") # the second one
im.save('/home/udai/Documents/Learn/lang-python/temp2.jpg')

text = pytesseract.image_to_string(Image.open('/home/udai/Documents/Learn/lang-python/temp2.jpg'))

print(text)
