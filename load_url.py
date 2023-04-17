"""Load a webpage."""
# https://python.langchain.com/en/latest/modules/agents/tools/examples/requests.html?highlight=webpage#requests
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.utilities import TextRequestsWrapper
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Load default environment variables (.env)
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

requests = TextRequestsWrapper()
content = requests.get("https://www.theonion.com/")

first_four_letters = content[:4]

print(first_four_letters)

chat = ChatOpenAI(temperature=0)

messages = [
    SystemMessage(content=f"You are a helpful assistant that answers questions about the following web page: {content}"),
    HumanMessage(content="What is a headline from the web page?")
]

# print(chat(messages))
