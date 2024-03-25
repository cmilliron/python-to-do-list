import streamlit as st
from PIL import Image

with st.expander("Starting Camera"):
    photo = st.camera_input("Camera")
# print(photo)

if photo:
    img = Image.open(photo)
    gray_img = img.convert('L')
    st.image(gray_img)