import os
from typing import Dict

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class MCPRequest(BaseModel):
    prompt: str
    context: Dict[str, str] = {}


app = FastAPI()


@app.post("/mcp/infer")
async def mcp_infer(req: MCPRequest):
    input_prompt = req.prompt
    input_context = req.context

    context_intro = "Context:\n"
    for key, value in input_context.items():
        context_intro += f"{key}: {value}\n"

    full_prompt = f"{context_intro}\nUser: {input_prompt}\nAI:"

    try:
        chat_response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that uses user context.",
                },
                {"role": "user", "content": full_prompt},
            ],
        )

        reply = chat_response.choices[0].message.content.strip()

        return {"reply": reply.strip(), "context_used": input_context}

    except Exception as e:
        print(f"Exception:{str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
