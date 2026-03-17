# 🤵 MedSpa Booking Automator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Docker Ready](https://img.shields.io/badge/docker-ready-blue.svg)]()

A production-grade, AI-powered micro-SaaS designed to convert missed calls into confirmed bookings for luxury MedSpas. Built on the principles of high-conversion automation and reliable, "deploy-your-own" architecture.

---

## 🚀 The Mission

Local MedSpas lose nearly **40% of potential bookings** due to missed calls after hours or during peak times. The **MedSpa Booking Automator** solves this by:
1.  **Detecting** missed calls via Twilio/VAPI.
2.  **Engaging** the lead immediately via automated SMS/WhatsApp.
3.  **Triaging** the request using a luxury-tuned AI Agent (GPT-4o).
4.  **Converting** the lead into a scheduled appointment via Calendly/GHL.

---

## 🛠️ Tech Stack

-   **Backend:** FastAPI (Python 3.11)
-   **AI Engine:** OpenAI GPT-4o-mini (Luxury MedSpa Persona)
-   **Database:** PostgreSQL (Containerized)
-   **Mobile:** Flutter (iOS & Android)
-   **Integrations:** Twilio (SMS), Calendly/GoHighLevel (Booking)
-   **Infrastructure:** Docker & Docker Compose

---

## 📂 Project Structure

```text
├── src/
│   ├── backend/          # FastAPI API, Webhooks, AI Logic
│   ├── frontend/         # Next.js Lead Dashboard (Admin UI)
│   └── mobile/           # Flutter Cross-Platform Application
├── specs/                # PRD and Technical Architecture
├── docker-compose.yml    # Production-ready orchestration
└── .env.example          # Environment configuration
```

---

## ⚡ Quick Start

### 1. Prerequisites
- Docker & Docker Compose installed.
- OpenAI API Key.
- Twilio Account (for SMS testing).

### 2. Environment Setup
Copy the example environment file and fill in your keys:
```bash
cp src/backend/.env.example src/backend/.env
```

### 3. Launch the Stack
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000`.

---

## 🤖 AI Agent Workflow

The system uses a custom **Luxury MedSpa Triage Agent** with the following logic:
1.  **Acknowledge:** "Hi! We noticed we just missed your call. How can we help you today?"
2.  **Service Identification:** Identifies if the client wants Botox, Fillers, Facials, or Laser treatments.
3.  **Booking Link:** Automatically provides the correct scheduling link based on the identified service.
4.  **Persistence:** Maintains a 10-message conversation memory for contextual follow-ups.

---

## 📱 Mobile App (Flutter)

The accompanying mobile application allows MedSpa owners to:
-   Monitor real-time AI conversations.
-   Manually intervene in high-value chats.
-   Track daily booking conversion metrics.
-   Receive push notifications for new leads.

---

## 📈 Roadmap

- [x] Phase 1: Architecture & Docker Setup
- [x] Phase 2: AI Triage Logic & Twilio Webhooks
- [ ] Phase 3: Calendly / GoHighLevel API Integration
- [ ] Phase 4: Next.js Dashboard Development
- [ ] Phase 5: Multi-tenancy & Authentication
- [ ] Phase 6: Mobile App (Flutter) Screen Implementation
- [ ] Phase 7: Production QA & Final Deployment

---

## 🤝 Contribution

This project is part of the **MoonLIT Arc** suite. For internal updates, contact the Lead Developer (**Alfred**).

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

Updated: 2026-03-17 by Alfred
