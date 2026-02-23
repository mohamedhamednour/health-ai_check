from langchain_mcp_adapters.client import MultiServerMCPClient
import sys


mcp_client = MultiServerMCPClient({
   
    "consultation_service": {
        "command": sys.executable,
        "args": ["-m", "mcp_core.consultation_mcp"],
        "transport": "stdio"
    }


})
    