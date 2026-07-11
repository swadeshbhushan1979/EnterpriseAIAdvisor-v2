from jira_client import JiraClient
import json

jira = JiraClient()

project = jira.get("/rest/api/3/project/KAN")

print(json.dumps(project, indent=2))