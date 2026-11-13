
from app.models.llm_model import llm_with_tools
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from app.services.tools.tool_registry import tool_registry
from pathlib import Path
from app.Exceptions.myExceptions import (
  ToolExecutionError
)

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

def llm_call(human_message: str):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=human_message)
    ]

    while True:

      ai_message = llm_with_tools.invoke(messages)

      messages.append(ai_message)

      if not ai_message.tool_calls:
        return ai_message.content

      print(ai_message.tool_calls)
      
      for tool_call in ai_message.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_id = tool_call["id"]

        tool = tool_registry.get(tool_name)

        if tool is None:
          raise ToolExecutionError(
            f"Invalid tool requested by LLM: '{tool_name}'"
          )
        else:
          try:
            result = tool.invoke(tool_args)
          except Exception as e:
            raise ToolExecutionError(
                    f"Tool '{tool_name}' execution failed: {str(e)}"
                  )

        
        tool_message = ToolMessage(
          content = str(result),
          tool_call_id = tool_id
        )

        messages.append(tool_message)
