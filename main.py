import os
from constants import openai_key #set your api_key in openai_key variable in constants file
from langchain.llms import OpenAI

import streamlit as st # type: ignore

os.environ["OPENAI_API_KEY"]=openai_key 

# Streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text=st.text_input("Search the topic you want")

## OpenAI LLMS
llm=OpenAI(temperature=0.8)  ##how much control the agent will have on the output, range 0-1,  more number,  more control

if input_text:
    st.write(llm(input_text))