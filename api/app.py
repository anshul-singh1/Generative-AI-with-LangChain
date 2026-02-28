from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or ""

# To see the langsmith trace logs in dashboard, use the env variable:
# LANGCHAIN_TRACING_V2=true and 
# LANGCHAIN_API_KEY=your_langchain_api_key


from langchain_ollama import OllamaLLM  # LangChainDeprecationWarning: The class `Ollama` was deprecated in LangChain 0.3.1 
                                        # and will be removed in 1.0.0. 
                                        # An updated version of the class exists in the `langchain-ollama package 
                                        # and should be used instead. 
                                        # To use it run `pip install -U `langchain-ollama` 
                                        # and import as `from `langchain_ollama import OllamaLLM``

from langchain_community.llms import Ollama

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

## Ollama
llm=Ollama(model="mistral")

prompt=ChatPromptTemplate.from_template("Write a poem in 50 words about {topic}")

add_routes(
    app,
    prompt|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost", port=8000)


