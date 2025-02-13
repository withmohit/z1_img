from PIL import Image
import io
import os

IMAGE_SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]
OUTPUT_DIR = "resized_images"

def process_images(upload_file):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image = Image.open(upload_file.file)
    resized_images = {}

    for size in IMAGE_SIZES:
        img_resized = image.resize(size)
        img_path = f"{OUTPUT_DIR}/image_{size[0]}x{size[1]}.png"
        img_resized.save(img_path, format="PNG")
        resized_images[size] = img_path

    return resized_images
