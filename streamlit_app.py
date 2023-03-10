import pathlib

import streamlit as st

from winning_writing import render_winning_writing
from prompt_compiler import render_prompt_compiler

st.set_page_config("Prompt engineering")


def main():
    instructions_path = str(pathlib.Path(__file__).parent.resolve() / "landing_page.md")
    readme_text = st.markdown(file_content_to_string(instructions_path))

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose a section", ["Start here", "Winning Writing x ChatGPT", "Prompt compiler"],)
    if app_mode == "Welcome":
        st.sidebar.success("To continue select a section from the toolbar.")
    elif app_mode == "Winning Writing x ChatGPT":
        readme_text.empty()
        run_winning_writing()
    elif app_mode == 'Prompt compiler':
        readme_text.empty()
        run_prompt_compiler()


def run_winning_writing():
    render_winning_writing()

def run_prompt_compiler():
    render_prompt_compiler()


def file_content_to_string(path):
    with open(path, "r") as file:
        data = file.read()
    return data


if __name__ == "__main__":
    main()
