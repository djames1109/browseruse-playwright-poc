import asyncio

from services.agent_service import AgentService
from services.controller_service import setup_shopping_controller
from tasks.site_validation_task import site_validation_task


# Entrypoint of the application
async def main():
    controller = setup_shopping_controller()
    task = site_validation_task()

    agent = AgentService.create_agent(controller, task)
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)


asyncio.run(main())
