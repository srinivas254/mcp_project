import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from app.services.tools.tool_schemas import tools

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)

