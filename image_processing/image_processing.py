import time

from PIL import Image


def get_image(image_url):
    print(f"Opening the image from URL: {image_url}")
    return Image.open(image_url)


def open_image(image_url):
    image = get_image(image_url)
    image.show()
    return image


image_path = "img.png"
word_matrix = "word_matrix.png"
mask = "mask.png"
output = "output.png"

word_matrix_image = get_image(word_matrix)
i1_size = word_matrix_image.size

mask_image = get_image(mask)
i2_size = mask_image.size
mask_image = mask_image.resize(i1_size)

# Make the mask image opaque.
output_image = word_matrix_image
mask_image.putalpha(180)
output_image.paste(mask_image, (0, 0), mask_image)
output_image.save(output, "PNG")
output_image.show()
# Sleeping for 5 seconds
time.sleep(5)
# This will only close the close object not the Image window.
output_image.close()
