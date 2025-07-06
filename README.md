# Model Context Protocol (MCP) Server

This is to a simple create Model Context Protocol (MCP) server and add some basic functionality to understand how MCP works and to get hands-on experience.

- This server will take prompt and context like your name, App Name and session id
- Responds back with same details

## How to start MCP Server

0. Set up virtual environment

1. enable virtual environemnt and install dependencies by running below command

   `pip3 install -r requirements.txt`

2. Access API service specs by hitting the url

  `uvicorn mcp_server:app --reload`

## Test MCP Server

- Need to run `mcp_client.py` file to interact with MCP server by running `python mcp_client.py`
- Will get input prompt and context as response in the JSON format
- You can modify prompt or context in the file `mcp_client.py` if required
