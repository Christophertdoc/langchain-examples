"""Load a webpage."""
# References
# https://python.langchain.com/en/latest/modules/agents/tools/examples/requests.html?highlight=webpage#requests
# https://python.langchain.com/en/latest/modules/indexes/text_splitters/getting_started.html
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.utilities import TextRequestsWrapper
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load default environment variables (.env)
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

requests = TextRequestsWrapper()
content = requests.get("https://www.theonion.com/")

truncated_content = content[:8000]

# print(truncated_content)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 20,
    length_function = len,
)

texts = text_splitter.create_documents([content])
# print(texts[0])
# print(texts[1])


chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(content=f"You are a helpful assistant that answers questions about the following web page: {truncated_content}"),
    HumanMessage(content="What is the title of the web page?")
]

print(chat(messages))

# LEFT OFF AT LOADING A LARGE WEBPAGE THROUGH INDEXING: https://python.langchain.com/en/latest/modules/indexes/getting_started.html