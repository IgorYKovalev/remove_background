from rembg import remove
from PIL import Image

input_path = '/Users/kovalevigor/PycharmProjects/remove_background/images.jpg'
output_path = 'image_no_bg.png'

with Image.open(input_path) as file:
    file.load()

output = remove(file, bgcolor=(234, 74, 136, 255))
# output = remove(file, only_mask=True)

output.save(output_path)
