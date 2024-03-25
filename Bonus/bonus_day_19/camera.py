import streamlit as st
from PIL import Image


def process_image(photo_to_convert):
    img = Image.open(photo_to_convert)
    gray_img = img.convert('L')
    st.image(gray_img)


uploaded_photo = st.file_uploader("Upload Image", key="uploaded")

with st.expander("Starting Camera"):
    photo = st.camera_input("Camera", key='from_camera')
# print(photo)

if st.session_state['uploaded']:
    process_image(st.session_state['uploaded'])
elif st.session_state['from_camera']:
    process_image(st.session_state['from_camera'])