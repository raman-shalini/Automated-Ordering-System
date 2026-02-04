from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent_executor
from consent import verify_consent

app = FastAPI(title="Agentic AI Assistant")

class UserQuery(BaseModel):
    message: str

@app.post("/chat")
def chat(query: UserQuery):
    response = agent_executor.run(query.message)

    if not verify_consent(query.message):
        return {
            "status": "awaiting_consent",
            "response": response
        }

    return {
        "status": "consent_received",
        "response": response
    }
