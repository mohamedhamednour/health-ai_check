from langchain_ollama import ChatOllama

from llm.agent.create_agent import make_agent

class HandlerAISummary:

    def __init__(self, prompt_id):
        self.prompt_id = prompt_id
        self.llm =  ChatOllama(
        model="glm-5:cloud",
        temperature=0,
        timeout=120,
    )
    
    async def handle_llm(self):
    # Await the async function make_agent
        agent_executor = await make_agent(self.llm)
        response = await agent_executor.ainvoke({"input": f"what is the patient's name? has id  {self.prompt_id}"})
        print(response['output'] , 'sssssssssssssss')
        return response['output']




    