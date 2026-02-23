import logging
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from mcp_core.server.consultation_service import mcp_client as tools_mcp
from llm.prompts.consultation_prompt import prompt
import traceback

# Setup Logger
logger = logging.getLogger("make_agent")
logger.setLevel(logging.DEBUG)

async def make_agent(llm):
    try:
        logger.info("Fetching tools from MCP client...")
        client = tools_mcp
        
        # We don't use 'async with client' here because it would close the connection
        # before the agent executor can use the tools.
        # The client should be managed at a higher level or left open for the session.
        tools = await client.get_tools()

        # create_tool_calling_agent is generally faster and more reliable
        agent = create_tool_calling_agent(
            llm=llm,
            tools=tools,
            prompt=prompt,
        )        
        
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5, 
        )

        return agent_executor

    except Exception as e:
        logger.error("Agent creation failed!")
        logger.error(str(e))
        logger.error(traceback.format_exc())
        raise