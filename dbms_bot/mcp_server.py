"""MCP server exposing the DBMS tools (MCPServer from the official `mcp` SDK, v2).

Run:  python -m dbms_bot.mcp_server          (stdio, spawned by the agent)
      python -m dbms_bot.mcp_server --http   (streamable HTTP on localhost:8765)
"""

import sys

from mcp.server.mcpserver import MCPServer

from dbms_bot import tools

mcp = MCPServer("dbms-study-assistant")

# Each tool is a thin wrapper; the docstring becomes the description the model sees.
mcp.tool()(tools.search_notes)
mcp.tool()(tools.answer_question)
mcp.tool()(tools.explain_topic)
mcp.tool()(tools.generate_quiz)
mcp.tool()(tools.summarize_topic)

if __name__ == "__main__":
    if "--http" in sys.argv:
        mcp.run(transport="streamable-http", port=8765)
    else:
        mcp.run(transport="stdio")
