# 🌾 KrishiMitro (Fosholer Chikitsha) — Demonstration & Pitch Playbook

A structured walkthrough and product pitch guide for **KrishiMitro — Fosholer Chikitsha**, showcasing autonomous multi-step reasoning, on-field leaf pathology diagnosis, climate-aware crop scheduling, and deterministic farm economics.

---

## ⏱️ Pre-Demo Setup & Verification
- [ ] Environment active: `source .venv/bin/activate`
- [ ] Knowledge base verified: `cd backend && python -m app.rag.ingest` (195 chunks / 19 documents indexed)
- [ ] Application running: `uvicorn app.main:app --port 8000`
- [ ] Open in browser: **http://localhost:8000**
- [ ] Verify `.env` contains an active `GEMINI_API_KEY` (Free Tier) or `OPENAI_API_KEY`
- [ ] Click **"New farm"** in the UI header to clear local session memory and start clean.

---

## 🎤 30-Second Elevator Pitch
> *"Smallholder farmers face unpredictable climate shifts, volatile input costs, and devastating pest outbreaks without timely access to agronomic experts. Standard chatbots offer generic, hallucinated text that farmers cannot risk their livelihoods on. **KrishiMitro** is an autonomous AI agronomist that combines computer vision for instant leaf disease diagnosis with deterministic mathematical engines and verified government research. It turns an empty field into an itemized, weather-aware season plan, complete with water-saving AWD mapping and transparent, auditable decision trails."*

---

## ▶️ 4-Minute Interactive Demonstration Flow

### Step 1: Natural Conversational Intake & Geospatial Soil Auto-Detection
- **User Prompt:** *"I have 2 acres in Bogura, budget 80,000 BDT, planning for this winter (Rabi) season. What should I grow?"*
- **What to Highlight in the Live Trace Panel:**
  - `geocode_location`: Resolves Bogura coordinates via Open-Meteo.
  - `lookup_soil_texture`: Automatically samples SRDI digital raster maps to detect **Clay Loam (দোআঁশ)** soil—without questioning or confusing the farmer with technical soil surveys.
  - `get_weather_forecast`: Retrieves live 14-day rainfall and temperature distributions.
  - Demonstrates that the agent collects missing parameters intelligently rather than running an exhaustive questionnaire.

### Step 2: Multi-Crop Comparative Ranking with Deterministic Economics
- The agent analyzes agro-climatic suitability and presents 3 optimal candidate crops (e.g., Potato, Wheat, Mustard).
- **Core Value:** Each crop is ranked by suitability, water requirement, operational risk, and projected net profit computed by `compute_financials`.
- Show that modifying the budget or land area recalculates itemized expenditure, expected harvest yield, and return on investment (ROI) via pure Python algorithms.

### Step 3: Validated Season Calendar Generation
- **User Prompt:** *"Build me the complete season plan for Potato."*
- **Outcome:** The agent executes `generate_season_plan` to construct a chronologically validated timeline:
  - Land preparation & basal fertilizer placement.
  - Sowing & seed tuber depth.
  - Nitrogen (Urea) top-dressing split dates.
  - Irrigation schedules and late-blight scouting checkpoints.
  - Harvest and skin-curing timelines.

### Step 4: Climate-Smart Irrigation via AWD Suitability Mapping
- **User Prompt:** *"How can I cut my irrigation and pumping costs?"*
- **Outcome:** For paddy crops, the agent queries `lookup_awd_suitability` against BRRI/IRRI spatial rasters.
- Quantifies that the farm is suitable for Alternate Wetting and Drying (AWD), forecasting a **25%–30% reduction** in water pumping fuel and electricity expenses.

### Step 5: Multimodal Plant Disease Diagnosis (Computer Vision)
- Click the camera button (📷) to upload a field photo of an infected leaf (e.g., late blight or blast lesion).
- **Outcome:** Multimodal vision identifies visible pathology, provides English and Bengali disease taxonomy, assigns a confidence level, and retrieves vetted Integrated Pest Management (IPM) chemical and organic treatment protocols.

### Step 6: Proactive Meteorological Schedule Alarms
- Direct attention to the notification banner at the top of the interface:
- If unseasonal heavy rainfall is predicted within 72 hours of a scheduled nitrogen application, the system proactively generates a banner notification recommending postponing fertilization to prevent nutrient runoff and cost wastage.

### Step 7: Official Extension Helpline Integration
- **User Prompt:** *"I need to speak directly with an agriculture officer."*
- **Outcome:** Renders an instant one-tap dialer chip linking to the official National Agriculture Call Center (**📞 16123**).

### Step 8: Seamless Telco Micro-Payment Simulation
- Farmers can purchase seeds and fertilizers through an integrated cart modal, triggering bdapps Charging-as-a-Service (CaaS) mobile balance deduction and SMS invoice delivery.

---

## 🛡️ Strategic Q&A for Investors, Judges, and Partners

| Common Inquiry | Technical Reality & Competitive Edge |
|---|---|
| **"How do you prevent dangerous AI hallucinations in fertilizer dosages and finances?"** | The LLM is strictly prohibited from performing arithmetic or dosage synthesis. All financial figures, break-even thresholds, fertilizer splits, and crop durations are executed in deterministic Python modules backed by 67 automated unit tests. |
| **"Where does the agronomic knowledge originate?"** | Grounded in 19 verified government manuals from apex institutions: BARC (FRG 2024), BRRI, SRDI, DAE, BBS, and DAM. |
| **"How does the system perform in low-connectivity rural settings?"** | GIS rasters are pre-baked into lightweight spatial JSON grids ($O(1)$ lookup time), weather queries feature local caching, and the interface is designed as lightweight vanilla JS. |
| **"Is farmer data preserved across devices?"** | State is persisted in a local SQLite database indexed by session ID, allowing farmers to refresh or return weeks later without losing their profile. |
