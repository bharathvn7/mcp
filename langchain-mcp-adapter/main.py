import asyncio
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/bharath.narendra/learning/mcp-server/mcp-servers/langchain-mcp-adapter/servers/math_server.py"],

)


async def main():
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 2+2")]})
            print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())

