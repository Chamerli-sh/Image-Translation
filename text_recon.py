from PIL import Image
import pytesseract

img = Image.open('assets/f.jpeg')
result = pytesseract.image_to_string(img, lang='eng')
print(result)

with open('text_result.txt', mode ='W') as file:
    file.write(result)
    print("ready!")