import asyncio

from services.agent_service import AgentService
from tasks.site_validation_task import site_validation_task


# Entrypoint of the application
async def main():
    task = site_validation_task()
    agent = AgentService.create_agent(task)
    await agent.run(max_steps=20)


asyncio.run(main())
