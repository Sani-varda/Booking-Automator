from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI(title="MedSpa Booking Automator API")

class WebhookPayload(BaseModel):
    # This will be expanded for Twilio/VAPI specific schemas
    event: str
    from_number: str
    to_number: str

@app.get("/")
async def root():
    return {"status": "online", "service": "MedSpa Booking Automator"}

@app.post("/webhooks/missed-call")
async def handle_missed_call(request: Request):
    # Log missed call and trigger AI response
    form_data = await request.form()
    from_number = form_data.get("From")
    print(f"📞 Missed call detected from: {from_number}")
    
    # Logic for triggering SMS response via Twilio will go here
    return {"message": "webhook received"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
