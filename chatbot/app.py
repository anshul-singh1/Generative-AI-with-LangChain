from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please Response to the user query in a concise manner."),
        ("user", "Question:{question}")
    ]
)


## streamlit framework

st.title('Langchain Demo with Ollama')
input_text = st.text_input("search the topic you want to know about")

# Ollama LLM : mistral 
llm = Ollama(model="mistral")
StrOutputParser= StrOutputParser()
chain = prompt | llm | StrOutputParser

if input_text:
    st.write(chain.invoke({"question": input_text}))
    
