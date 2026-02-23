import asyncio
from llm.agent.create_agent import make_agent
from langchain_ollama import ChatOllama

async def run_test():
    llm = ChatOllama(
        model="glm-5:cloud",
        temperature=0,
        timeout=120,
    )

    # Await the async function make_agent
    agent_executor = await make_agent(llm)
    
    # Use ainvoke for async agent execution
    response = await agent_executor.ainvoke({"input": "what is the patient's name? has id 96b67236-8edf-41bc-8e76-8c0a3ea6b6b8"})
    print(response['output'] , 'sssssssssssssss')

if __name__ == "__main__":
    asyncio.run(run_test())