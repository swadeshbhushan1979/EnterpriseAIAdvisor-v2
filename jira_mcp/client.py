import asyncio
import os

print("=" * 80)
print("CUSTOM CLIENT.PY LOADED")
print("FILE:", __file__)
print("=" * 80)

from fastmcp import Client, __version__
#from fastmcp.client.transports import StdioTransport

SERVER_FILE = os.path.join(
    os.path.dirname(__file__),
    "server.py"
)

# transport = StdioTransport(
#     command="fastmcp",
#     args=["run", SERVER_FILE]
# )

print("FastMCP Version:", __version__)

client = Client("https://jira-mcp-server-ckgn.onrender.com/mcp")

print("CLIENT CREATED")

#client = Client(transport)


async def create_task(summary, description):

    async with client:

        result = await client.call_tool(
            "create_story",
            {
                "summary": summary,
                "description": description
            }
        )

        return result.data


def create_task_sync(summary, description):

    return asyncio.run(
        create_task(
            summary,
            description
        )
    )