import asyncio
from fastmcp import Client

async def main():
    async with Client("mcp_server.py") as mcp_client:
        # list all tools
        tools = await mcp_client.list_tools()
        print("Available tools:", tools)

if __name__ == "__main__":
    test = asyncio.run(main())