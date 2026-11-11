from app.services.tools.tool_functions import query_postgres, search_github, get_sentry_errors

tool_registry = {
    "query_postgres":query_postgres,
    "search_github":search_github,
    "get_sentry_errors":get_sentry_errors
}