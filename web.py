import streamlit as st
import functions

todos = functions.get_todos_from_file()

def add_button_click():
    pass


def add_todo():
    todo = st.session_state['new_todo']
    print(todo)
    todos.append(todo + "\n")
    print(todos)
    functions.save_todos_to_files(todos)
    st.session_state['new_todo'] = ""


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')



if len(todos) == 0:
    st.write("Nothing todo.")
else:
    for item in todos:
        st.checkbox(item)

st.text_input(label="Enter a todo:",
              placeholder="Add New Todo...",
              label_visibility='hidden',
              key="new_todo",
              on_change=add_todo)

st.button(label='Add', on_click=add_todo)

st.session_state