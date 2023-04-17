"""Load a webpage."""
# References
# https://python.langchain.com/en/latest/modules/agents/tools/examples/requests.html?highlight=webpage#requests
# https://python.langchain.com/en/latest/modules/models/chat/examples/streaming.html
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.utilities import TextRequestsWrapper
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

# Load default environment variables (.env)
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

requests = TextRequestsWrapper()
content = requests.get("https://www.theonion.com/")

truncated_content = content[:8000]

print(truncated_content)

chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(content=f"You are a helpful assistant that answers questions about the following web page: {truncated_content}"),
    HumanMessage(content="What is the title of the web page?")
]

print(chat(messages))
