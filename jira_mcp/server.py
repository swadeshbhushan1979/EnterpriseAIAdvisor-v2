from fastmcp import FastMCP
from jira_mcp.jira_client import JiraClient

jira = JiraClient()

mcp = FastMCP("Enterprise Jira MCP")


@mcp.tool
def list_projects():

    return jira.list_projects()

@mcp.tool
def issue_types():

    return jira.issue_types()

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
if __name__ == "__main__":
    mcp.run()