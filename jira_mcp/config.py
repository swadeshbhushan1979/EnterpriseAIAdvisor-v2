"""
Enterprise Jira MCP Server
Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # -----------------------
    # Jira
    # -----------------------

    JIRA_URL = os.getenv("JIRA_URL", "").rstrip("/")

    JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")

    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")

    JIRA_PROJECT = os.getenv("JIRA_PROJECT", "")

    # -----------------------
    # Validation
    # -----------------------

    @classmethod
    def validate(cls):

        missing = []

        if not cls.JIRA_URL:
            missing.append("JIRA_URL")

        if not cls.JIRA_EMAIL:
            missing.append("JIRA_EMAIL")

        if not cls.JIRA_API_TOKEN:
            missing.append("JIRA_API_TOKEN")

        if not cls.JIRA_PROJECT:
            missing.append("JIRA_PROJECT")

        if missing:

            raise ValueError(
                "Missing configuration: "
                + ", ".join(missing)
            )