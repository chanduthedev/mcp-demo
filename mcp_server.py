from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class MCPRequest(BaseModel):
    prompt: str
    context: Dict[str, str] = {}


app = FastAPI()


@app.post("/mcp/infer")
async def mcp_infer(req: MCPRequest):
    input_prompt = req.prompt
    input_context = req.context

    user = input_context.get("user", "unknown")
    app_name = input_context.get("app_name", "default-app")

    reply = f"From {app_name}, Hello {user}, you asked: {input_prompt}"

    return {"reply": reply, "context_used": input_context}
