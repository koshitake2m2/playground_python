from typing import Final
from dataclasses import dataclass
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()
# OPENAI_API_KEY: Final[str] = os.environ.get('OPENAI_API_KEY', 'ww')
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


@dataclass(frozen=True)
class ChatService:
  def chat(self, msg) -> str:
    model = ChatOpenAI(model='gpt-3.5-turbo')
    messages = [
        SystemMessage(content="You are an English teacher."),
        HumanMessage(content=msg),
    ]


    model.invoke(messages)

if __name__ == "__main__":
  chat_service = ChatService()
  answer = chat_service.chat('Hello! How are you?')
  print(answer)
