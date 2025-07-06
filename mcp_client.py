import uuid

import requests


def send_mcp_request(prompt: str, req_context=None):
    url = "http://localhost:8000/mcp/infer"
    payload = {"prompt": prompt, "context": req_context or {}}

    response = requests.post(url, json=payload)

    return response.json()


if __name__ == "__main__":
    session_id = str(uuid.uuid4())
    context = {
        "user": "chanduthedev",
        "app_name": "MCP-Demo-App",
        "session_id": session_id,
    }

    prompt = "What's the weather like today"
    result = send_mcp_request(prompt, context)
    print("MCP Response:", result)
