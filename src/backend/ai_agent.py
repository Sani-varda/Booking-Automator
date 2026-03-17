import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BookingAgent:
    """AI Agent for triage and service selection for MedSpas"""
    
    SYSTEM_PROMPT = (
        "You are an AI assistant for a luxury MedSpa. Your goal is to capture leads from missed calls. "
        "Be professional, warm, and efficient. "
        "Process: 1. Acknowledge the missed call. 2. Ask which service they are interested in (Botox, Fillers, Facials, Laser). "
        "3. Once a service is identified, provide the Calendly link for booking. "
        "Keep responses short and suitable for SMS."
    )

    def generate_response(self, customer_message: str, conversation_history: list = None):
        if not conversation_history:
            conversation_history = []
        
        messages = [{"role": "system", "content": self.SYSTEM_PROMPT}]
        messages.extend(conversation_history)
        messages.append({"role": "user", "content": customer_message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=150
        )
        
        return response.choices[0].message.content

agent = BookingAgent()
