from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from llm.prompts.base_format import SYSTEM_PROMPT
from llm.prompts.guideline import GuidLines

COMPLETE_SYSTEM_PROMPT = (
    SYSTEM_PROMPT + 
    GuidLines
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", COMPLETE_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
