import PIL.Image as piii
import os
import google.generativeai as genai

import os
from PIL import Image

# Path to the directory containing images
directory_path = r'C:\Users\sriharsha\Desktop\repos\emoji'

# List all files in the directory
files = os.listdir(directory_path)

# Filter out all image files (assuming JPEG and PNG files)
image_files = [file for file in files if file.endswith(('.jpg', '.png'))]

# Dictionary to hold image objects
images = {}

# Open each image and store it in a dictionary
for image_file in image_files:
    file_path = os.path.join(directory_path, image_file)
    images[image_file] = Image.open(file_path)

images_names = []
for image_name, image in images.items():
    images_names.append(str(image_name))
    # print(f"Processing {image_name}")


sample_paths = [piii.open(i) for i in images_names]


model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt ="""
You are an expert data scientist in analysis of visualization and extract meaningful insights by considering the following aspects:
1. You will always make sure about the type of visualizations and graphs
2. Extracts the meaningful analytics from the images by proper analysis and understanding of the image
3. Make sure to check on the features analysed and respond accordingly with proper context
"""

response = model.generate_content([prompt]+[i for i in sample_paths])

print(response.text)