from jira_client import JiraClient

jira = JiraClient()

result = jira.create_issue(
    summary="AI Test Story",
    description="Created from Python",
    issue_type="Task"
)

print(result)