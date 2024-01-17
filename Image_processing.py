from PIL import Image, ImageDraw
import json
import pytesseract
import matplotlib.pyplot as plt

with open('config.json') as config_file:
    config = json.load(config_file)

pytesseract.pytesseract.tesseract_cmd = config["tesseract_path"]

image_path = config['image_path']
img = Image.open(image_path)

roi_coordinates = tuple(config['roi_coordinates'])

draw = ImageDraw.Draw(img)

draw.rectangle(roi_coordinates, outline='red', width=2)

roi_img = img.crop(roi_coordinates)

text = pytesseract.image_to_string(roi_img)

print(text)

plt.imshow(img)
plt.title('Image with ROI Box')
plt.show()

plt.imshow(roi_img)
plt.title('Cropped Region')
plt.show()
