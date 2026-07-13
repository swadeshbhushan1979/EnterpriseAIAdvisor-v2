"""
Enterprise Jira MCP Tools
Version 2.0
"""

from fastmcp import FastMCP

from jira_client import JiraClient

jira = JiraClient()

mcp = FastMCP(
    name="Enterprise Jira MCP"
)


@mcp.tool
def list_projects():

    return jira.list_projects()


@mcp.tool
def search_issues(jql: str):

    return jira.search(jql)


@mcp.tool
def get_issue(issue_key: str):

    return jira.issue(issue_key)


@mcp.tool
def create_story(

    summary: str,

    description: str

):

    return jira.create_issue(

        summary,

        description,

        issue_type="Task"

    )