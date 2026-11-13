from app.services.tools.tool_functions import (
    query_postgres,
    search_github,
    get_sentry_errors
)

tools = [
    query_postgres,
    search_github,
    get_sentry_errors
]