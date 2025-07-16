from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

llm = ChatOpenAI()


async def main():
    
    client =  MultiServerMCPClient(
        {
            "math": {
                "command":"python",
                "args":["/Users/bharath.narendra/learning/mcp-server/mcp-servers/langchain-mcp-adapter/servers/math_server.py"],
                "transport": "stdio"
            }, 
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse"
            }
        }
    ) 

    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print(math_response)
    print(weather_response)

    
    
if __name__ == "__main__":
    asyncio.run(main())
