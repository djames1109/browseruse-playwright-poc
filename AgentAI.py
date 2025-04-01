import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

api_key = os.environ['GEMINI_API_KEY']
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro-exp-03-25', api_key=SecretStr(api_key))


async def main():
    task = "Compare the price of gpt-4o and DeepSeek-V3"
    agent = Agent(
        task=task,
        llm=llm
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
