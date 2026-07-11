"""
Enterprise Jira Client
Version 2.0
"""

import requests
from requests.auth import HTTPBasicAuth

from jira_mcp.config import Config


class JiraClient:

    def __init__(self):

        Config.validate()

        self.base_url = Config.JIRA_URL

        self.auth = HTTPBasicAuth(
            Config.JIRA_EMAIL,
            Config.JIRA_API_TOKEN
        )

        self.headers = {

            "Accept": "application/json",

            "Content-Type": "application/json"

        }

    # -------------------------------------------------------
    # Generic REST Methods
    # -------------------------------------------------------

    def get(self, endpoint):

        response = requests.get(

            self.base_url + endpoint,

            headers=self.headers,

            auth=self.auth

        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, payload):

        response = requests.post(
            self.base_url + endpoint,
            headers=self.headers,
            auth=self.auth,
            json=payload
        )

        print("STATUS:", response.status_code)
        print("BODY:", response.text)

        response.raise_for_status()

        return response.json()

    def put(self, endpoint, payload):

        response = requests.put(

            self.base_url + endpoint,

            headers=self.headers,

            auth=self.auth,

            json=payload

        )

        response.raise_for_status()

        return response.json()

    # -------------------------------------------------------
    # Projects
    # -------------------------------------------------------

    def list_projects(self):

        return self.get("/rest/api/3/project")

    # -------------------------------------------------------
    # Issue Types
    # -------------------------------------------------------

    def issue_types(self):

        return self.get("/rest/api/3/issuetype")

    # -------------------------------------------------------
    # Search
    # -------------------------------------------------------

    def search(self, jql):

        payload = {

            "jql": jql,

            "maxResults": 100

        }

        return self.post(

            "/rest/api/3/search/jql",

            payload

        )

    # -------------------------------------------------------
    # Issue
    # -------------------------------------------------------

    def issue(self, key):

        return self.get(

            f"/rest/api/3/issue/{key}"

        )

    # -------------------------------------------------------
    # Create Issue
    # -------------------------------------------------------

    def create_issue(
        self,
        summary,
        description,
        issue_type="Task"
    ):

        payload = {
            "fields": {
                "project": {
                    "key": Config.JIRA_PROJECT
                },
                "summary": summary,
                "issuetype": {
                    "name": issue_type
                },
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description
                                }
                            ]
                        }
                    ]
                }
            }
        }

        return self.post(
            "/rest/api/3/issue",
            payload
        )