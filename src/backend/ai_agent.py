import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class BookingAgent:
    """AI Agent for triage and service selection for MedSpas using Gemini"""
    
    SYSTEM_PROMPT = (
        "You are an AI assistant for a luxury MedSpa. Your goal is to capture leads from missed calls. "
        "Be professional, warm, and efficient. "
        "Process: 1. Acknowledge the missed call. 2. Ask which service they are interested in (Botox, Fillers, Facials, Laser). "
        "3. Once a service is identified, provide the Calendly link for booking. "
        "Keep responses short and suitable for SMS. Reply only with the message text."
    )

    def __init__(self):
        # Using Gemini 2.0 Flash for speed and efficiency
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=self.SYSTEM_PROMPT
        )

    def generate_response(self, customer_message: str, conversation_history: list = None):
        if not conversation_history:
            conversation_history = []
        
        # Convert simple history to Gemini content format
        chat_history = []
        for msg in conversation_history:
            role = "user" if msg["role"] == "user" else "model"
            chat_history.append({"role": role, "parts": [msg["content"]]})

        chat = self.model.start_chat(history=chat_history)
        response = chat.send_message(customer_message)
        
        return response.text.strip()

agent = BookingAgent()
