import asyncio
import os

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

SERVER_FILE = os.path.join(
    os.path.dirname(__file__),
    "server.py"
)

transport = StdioTransport(
    command="fastmcp",
    args=["run", SERVER_FILE]
)

client = Client(transport)


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