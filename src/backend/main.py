import os
import requests
import json
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from ai_agent import agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Booking Automator API")

# Simple in-memory conversation store (Replace with Redis/Postgres for production)
conversations = {}

class Message(BaseModel):
    role: str
    content: str

@app.post("/webhooks/twilio/sms")
async def handle_sms(From: str = Form(...), Body: str = Form(...)):
    """Handle incoming SMS from Twilio"""
    customer_number = From
    message_body = Body
    
    # Get or initialize history
    history = conversations.get(customer_number, [])
    
    # Generate AI Response
    ai_response = agent.generate_response(message_body, history)
    
    # Update History
    history.append({"role": "user", "content": message_body})
    history.append({"role": "assistant", "content": ai_response})
    conversations[customer_number] = history[-10:] # Keep last 10 messages
    
    print(f"💬 SMS from {customer_number}: {message_body}")
    print(f"🤖 AI Response: {ai_response}")
    
    # In a real setup, we'd trigger a Twilio SMS send here.
    # For now, we return it for the webhook response or testing.
    return {
        "to": customer_number,
        "message": ai_response
    }

@app.get("/conversations/{number}")
async def get_history(number: str):
    return conversations.get(number, [])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
