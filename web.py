import streamlit as st
import functions

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

todos = functions.get_todos_from_file()

if len(todos) == 0:
    st.write("Nothing todo.")
else:
    for item in todos:
        st.checkbox(item)

st.text_input(label="Enter a todo:",
              placeholder="Add New Todo...",
              label_visibility='hidden')

st.button(label='Add', )