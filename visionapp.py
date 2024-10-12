from dotenv import load_dotenv

load_dotenv() # load all the variables from .env 

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = "AIzaSyBHTV8_2Ul2nrKdLEht5BKWbQEkgIZvqIA")

#function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_respose(input,image,prompt):

    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


#Sreamlit Setup

st.set_page_config(page_title = "Tagline Generator for instagram posts")

st.header("Tagline Generator for instagram posts")

input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of your choice..",type=['jpg','jpeg','png'])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded Image",use_column_width=True)

submit = st.button("Generate Tag line")

input_prompt = """
You are an expert data scientist in analysis of visualization and extract meaningful insights by considering the following aspects:
1. You will always make sure about the type of visualizations and graphs
2. Extracts the meaningful analytics from the images by proper analysis and understanding of the image
3. Make sure to check on the features analysed and respond accordingly with proper context
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_respose(input_prompt,image_data,input)
    st.subheader("The Response is : ")
    st.write(response)

