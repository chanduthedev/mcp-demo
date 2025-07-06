# Model Context Protocol (MCP) Server

This is to a simple create Model Context Protocol (MCP) server and add some basic functionality to understand how MCP works and to get hands-on experience.

- This server will take prompt and context like your name, App Name and session id
- Responds back with same details

## How to start MCP Server

Step 0.
- Set up virtual environment and enable virtual environment
- Create new `.env` file, copy content from `env` file and update API Key

Step 1.
- Install dependencies by running below command

  `pip3 install -r requirements.txt`

Step 2.
- Run below command to start the server

`uvicorn mcp_server:app --reload`

Step 3.
- Access below url to see available API points

`http://localhost:8000/docs`

## Test MCP Server

- Need to run `mcp_client.py` file to interact with MCP server by running `python mcp_client.py`
- Will get input prompt and context as response in the JSON format
- You can modify prompt or context in the file `mcp_client.py` if required
