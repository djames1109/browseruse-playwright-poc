import os
import sys

from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


class AgentService:

    @staticmethod
    def create_agent(use_vision: bool = True):
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        load_dotenv()

        # Retrieve Azure-specific environment variables
        azure_openai_api_key = os.getenv('AZURE_OPENAI_API_KEY')
        azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

        if not azure_openai_api_key or not azure_openai_endpoint:
            raise ValueError('AZURE_OPENAI_API_KEY or AZURE_OPENAI_ENDPOINT is not set')

        # Initialize the Azure OpenAI client
        llm = AzureChatOpenAI(
            model_version='gpt-4o-mini',
            api_key=azure_openai_api_key,
            azure_endpoint=azure_openai_endpoint,  # Corrected to use azure_endpoint instead of openai_api_base
            azure_deployment='gpt-4o-mini',  # Use deployment_name for Azure models
            api_version='2024-12-01-preview',  # Explicitly set the API version here
        )

        agent = Agent(
            task='Go to google.com and search for best anime series.'
                 'click the first link result.',
            llm=llm,
            use_vision=use_vision,
        )

        return agent
