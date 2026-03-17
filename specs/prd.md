# PRD: MedSpa Booking Automator

## 1. Objective
A production-grade micro-SaaS designed to automate missed-call-to-booking flows for MedSpas. The goal is to capture high-intent leads who call after hours or during busy times and convert them into scheduled appointments via automated SMS/WhatsApp.

## 2. Core Features
- **Missed Call Trigger:** Detect missed calls via Twilio/VAPI.
- **AI Triage (SMS/WhatsApp):** Instant automated response asking for the desired service.
- **Booking Integration:** Connect to Calendly/GoHighLevel for real-time scheduling.
- **Lead Dashboard:** Simple UI to view conversation history and booking status.
- **Multi-Tenant Ready:** Designed for deployment across multiple MedSpa locations.

## 3. Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL (via Supabase or local Docker)
- **Frontend:** Next.js (React)
- **Integrations:** Twilio (SMS/Voice), Calendly (Booking), OpenAI (AI Logic)
- **Deployment:** Docker (based on Atarity/deploy-your-own-saas principles)

## 4. Implementation Phases (7-Day Sprint)
1. **Day 1:** System Architecture & Missed Call Webhook (Twilio).
2. **Day 2:** AI Agent logic for conversation handling.
3. **Day 3:** Calendly API Integration.
4. **Day 4:** Next.js Dashboard (Lead Tracking).
5. **Day 5:** Multi-tenancy & Auth implementation.
6. **Day 6:** End-to-End Testing & QA.
7. **Day 7:** Production Deployment & Handoff.
