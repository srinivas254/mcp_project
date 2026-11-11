
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_postgres",
            "description": "Execute a read-only SQL query",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_github",
            "description": "Search GitHub repository information",
            "parameters": {
                "type": "object",
                "properties": {
                    "repo": {"type": "string"}
                },
                "required": ["repo"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sentry_errors",
            "description": "Retrieve recent errors from Sentry",
            "parameters": {
                "type": "object",
                "properties": {
                    "project": {"type": "string"}
                },
                "required": ["project"]
            }
        }
    }
]