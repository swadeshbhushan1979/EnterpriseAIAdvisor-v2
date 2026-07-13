import asyncio
from fastmcp import Client

async def main():
    client = Client("https://jira-mcp-server-ckgn.onrender.com/mcp")

    print("Client:", client)

    async with client:
        print("Connected!")
        tools = await client.list_tools()
        print(tools)

asyncio.run(main())