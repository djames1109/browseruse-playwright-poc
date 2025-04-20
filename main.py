import asyncio

from services.agent_service import AgentService


async def main():
    agent = AgentService.create_agent()
    await agent.run(max_steps=10)
    input('Press Enter to continue...')


asyncio.run(main())
