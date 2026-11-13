from app.services.tools.tool_schemas import tools

tool_registry = {
    tool.name : tool
    for tool in tools
}