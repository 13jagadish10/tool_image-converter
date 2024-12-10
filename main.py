# By default it converts the jpg, jpeg, png images to webp
import os
from PIL import Image

def convert_jpg_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            webp_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')
            img.save(webp_path, 'webp')
            print(f"Converted {filename} to {webp_path}")

input_folder = './input' 
output_folder = './output'
convert_jpg_to_webp(input_folder, output_folder)
