import streamlit as st
import pathlib
from PIL import Image

import pandas as pd

def render_winning_writing():

    st.write(
      """
    # Winning Writing

    *Background*: I taught a session on prompt engineering for Glenn Kramon's Winning Writing class at the Stanford Graduate School of Business (GSB).
        The course focuses on techniques for writing better professionally — memos, emails, cold-call letters, 
        speeches, feedback for colleagues, news releases, responses to questions from the media and from interviewers, 
        and opinion pieces.
    """
    )
    st.video("https://youtu.be/MHrFE4AR4OY")

    st.write(
        '''
        *Assorted resources*:
        [Complete slides from the class presentation](https://docs.google.com/presentation/d/10Ztf1gIPjCfrWfTK8UWwNujuw882obgYykKnzWuoLyQ/edit?usp=sharing)

        ### Prompt engineering (non-exhaustive advice)

        #### Guiding lesson
        - Treat ChatGPT (and other LLMs) as **your own personal army of semi-competent interns**
        - Use what it generates as a foundation to create new ideas and structures, then edit
        '''
    )

    st.image("https://lh3.googleusercontent.com/-gYzo8YngFx-vnve9c3_TafIzXdDITdwEuz-YAOEQC8PD-7B5NdVNVL4swvGn41HIc1GHgWC4Mcozi1Or63O3Cw-8ryXC7aZd205Q_Cg12bX_gdbRFck2Bx21vhN5kIHOS8QGZJV_uZiP0kErNf3yQ8BdQ=s2048", 
             caption="Smile! It's your own army of AI-generated interns!")
    
    st.write(
        '''
        - Prompt engineering is an art, rather than a science.
        - Many of these prompts work well as singular prompts, but you can (and should) continue to edit the initial output and iterate with additional prompting
          - For example, after ChatGPT's initial output: "I like that output, but could you condense the argument from the first paragraph?"
        '''
    )

    st.write(
        '''
        #### Other interesting prompts
        - **Condense or summarize a longer text**: “Succinctly summarize the following text into three paragraphs…”
        - **Beginning point of research**: “Can you provide me with a long and well-thought-out comprehensive yet simplified guide of [SUBJECT], that only includes offline information that you are certain is true and excludes any speculation or uncertainty? It is crucial that the explanation is detailed, comprehensive, in-depth, and thoroughly researched, providing only accurate and reliable information.”
        - **Generate email subject lines**: “Generate ten different interesting and engaging subject lines for the following email…”
        '''
    )

    st.write(
        '''
        #### Imagine you are...
        - A great way to improve the output is to append the sentence, “Imagine you are...”
        - A sample: “Imagine you are a talented analyst at a top-tier market research firm, a top graduate of Stanford Graduate School of Business. [QUESTION] Prioritize uncommon, expert advice.”
        '''
    )

    st.write(
        '''
        #### Prompt modifiers
         - **Modify the tone**: "Write the essay with a casual tone, written in a way that conveys warmth and competence."
         - **Mimic an author or a style**: "Write in the style of Shakespeare…” or "Pretend this piece is written by *The Economist*..."
         - **Specify the output length**: "... Ensure the output is under ten sentences" or "Write this in two to three paragraphs."
        '''
    )
