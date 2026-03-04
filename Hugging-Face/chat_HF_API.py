from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b", # ignore
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Capital of Uttarpradesh")

print(result.content)