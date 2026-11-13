from langchain.tools import tool

#query the pgsql database
@tool
def query_postgres(query: str):
    """Execute a read-only SQL query against PostgreSQL."""
    return {
        "database": "PostgreSQL",
        "result": [
            {"id": 1, "name": "Srinivas"},
            {"id": 2, "name": "Rahul"}
        ]
    }

#query the github repo
@tool
def search_github(repo: str):
    """Search for repository information on GitHub."""
    return {
        "repository": repo,
        "stars": 120,
        "open_issues": 8
    }

#query the sentry application
@tool
def get_sentry_errors(project: str):
    """Retrieve recent application errors from Sentry."""
    return {
        "project": project,
        "errors": [
            "Database connection timeout",
            "Internal Server Error"
        ]
    }