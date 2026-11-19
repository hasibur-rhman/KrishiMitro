# 🌾 KrishiMitro — Fosholer Chikitsha
### *AI-Powered Autonomous Agricultural Doctor & Climate-Smart Advisory Platform*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-3.8_Flash_(Free)-8E75C2.svg?logo=google&logoColor=white)](https://aistudio.google.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-Supported-412991.svg?logo=openai&logoColor=white)](https://platform.openai.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-orange.svg)](https://www.trychroma.com)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![Platform](https://img.shields.io/badge/Startup-Fosholer_Chikitsha-brightgreen.svg)](https://fosholerchikitsha.com)

---

## 📖 Executive Summary

**KrishiMitro — Fosholer Chikitsha (Crop Doctor)** is an enterprise-grade, autonomous agronomic advisory and digital healthcare platform designed specifically for smallholder farmers across South Asia. Engineered to scale the mission of the **Fosholer Chikitsha** startup initiative ([fosholerchikitsha.com](https://fosholerchikitsha.com/)), this platform bridges the gap between apex agricultural research institutes and rural farming communities.

Unlike standard conversational chatbots that hallucinate numerical estimates and dosage advice, this platform operates as a **Hybrid Autonomous Agent**:
- **Cognitive Layer:** Multi-step tool orchestration powered by **Google Gemini 3.8 Flash** (100% Free Tier) and **OpenAI GPT-4o / GPT-5.1**.
- **Computer Vision:** On-field leaf and plant disease pathology identification via multimodal vision.
- **Retrieval-Augmented Generation (RAG):** Grounded across 19 vetted governmental and scientific agricultural repositories.
- **Deterministic Algorithmic Engines:** Zero-hallucination pure Python engines handling farm economics, fertilizer dosage splits, and phenological calendars.
- **Geospatial Precomputation:** Offline raster-to-grid mapping for instant soil texture classification and water-saving irrigation suitability.
- **Full Traceability (XAI):** Real-time, transparent streaming of all agent tool invocations, parameters, latencies, and raw responses.

---

## 🚀 Core Capabilities

### 1. 🩺 AI Plant Disease Diagnosis (Computer Vision)
- Farmers upload or capture field photos of affected plant leaves directly from their mobile camera.
- Multimodal Vision AI (`gemini-3.8-flash` / `gpt-4o-mini`) inspects physical leaf symptoms (chlorosis, necrotic lesions, fungal mildew, insect boreholes), identifies the pathogen in both English and Bengali, and estimates confidence levels (Low / Medium / High).
- Diagnoses are automatically cross-referenced against vetted **Integrated Pest Management (IPM)** guidelines for recommended chemical, biological, and organic remedies.

### 2. 🐛 Weather & Phenology-Driven Pest Outbreak Risk Engine
- A deterministic multi-factor scoring matrix assesses imminent pest and fungal infestation risks by correlating real-time meteorological conditions (ambient temperature, humidity, 14-day rainfall forecasts from Open-Meteo) with the crop's active growth stage (seedling, tillering, flowering, tuber bulking).
- Delivers preemptive preventive measures and itemized per-acre treatment costs before infestations spread.

### 3. 📅 Dynamic, Weather-Adjusted Season Planning
- Generates a mathematically validated, chronologically sequenced crop calendar from land preparation to post-harvest curing.
- Computes critical milestones: basal fertilizer application, irrigation checkpoints, weeding intervals, and top-dressing splits.
- **Proactive Meteorological Alerts:** Background monitors match 14-day weather forecasts against planned operations, proactively issuing delay alerts (e.g., postponing nitrogen top-dressing before heavy rainfall to avoid leaching).

### 4. 🗺️ Geospatial Soil & AWD Irrigation Optimization
- **Automated Soil Texture Detection:** Farm GPS coordinates are sampled against high-resolution SRDI (Soil Resource Development Institute) rasters, calculating exact sand/silt/clay percentages and USDA soil triangle taxonomy without requiring manual farmer input.
- **AWD (Alternate Wetting and Drying) Suitability:** Integrates BRRI/IRRI spatial rasters to identify eligible paddy fields, quantifying water conservation and reducing irrigation pumping costs by 25–30%.

### 5. 💰 Deterministic Farm Financials & Scenario Modeling
- Strictly removes financial arithmetic from the LLM. An algorithmic engine calculates itemized operational expenditure (seeds, basal/top-dress fertilizers, labor, land prep, pesticides, irrigation), expected yield, gross revenue, net margin, ROI %, and break-even commodity pricing in local currency (BDT).
- **Scenario Simulation ("What-If"):** Recomputes financial exposure in real time against market shocks or weather variations via `yield_factor`, `cost_factor`, and `price_factor` parameters.

### 6. 📚 Evidence-Grounded RAG Knowledge Base
- ChromaDB persistent vector repository indexed over **19 verified public agricultural manuals & research guides**:
  - **BARC (Bangladesh Agricultural Research Council):** Fertilizer Recommendation Guide (FRG 2024)
  - **BRRI (Bangladesh Rice Research Institute):** Modern Rice Cultivation & Varietal Profiles
  - **SRDI (Soil Resource Development Institute):** Soil Fertility Atlas & Nutrient Depletion Maps
  - **DAE (Department of Agricultural Extension):** Agromet Bulletins & Plant Protection Compendiums
  - **BBS (Bangladesh Bureau of Statistics):** National Agricultural Statistics & Baseline Yields
  - **DAM (Department of Agricultural Marketing):** 8 Division-wise retail market price reports with historical trends
  - **DLS / BLRI:** Comprehensive livestock management, ration feeding, and vaccination schedules

### 7. 📲 Telco Charging & SMS Micro-Services (bdapps Integration)
- Standardized integration with the Robi/Axiata bdapps platform using **Charging-as-a-Service (CaaS)** and **SMS Gateway APIs**.
- Facilitates frictionless telco balance micro-payments for agricultural inputs, delivers verifiable digital SMS receipts, and broadcasts urgent weather warnings.

### 8. 🔍 Transparent Agent Observability (Explainable AI)
- Every internal decision, parameter passed, API response payload, and calculation latency is streamed live to the UI via an NDJSON event pipeline, allowing users, agronomists, and auditors to verify that every recommendation is rooted in verified data.

---

## 🏛️ System Architecture

```
                       [ Farmer / User ]
                              │
                 Web UI (Chat + Live Trace Panel)
                              │  Streaming (NDJSON)
                     FastAPI Backend Server
                              │
                Agentic Orchestrator (loop.py)
                [OpenAI Function Calling Engine]
                              │
     ┌───────────┬────────────┼────────────┬─────────────┬───────────┐
     ▼           ▼            ▼            ▼             ▼           ▼
  Geocoding &  ChromaDB   Deterministic   Spatial     Vision AI    bdapps
  Weather API     RAG     Engines (Math)  Grids       (Leaf Diag)  CaaS API
  (Open-Meteo) (19 Docs) (Finance/Pest)  (Soil/AWD)   (Gemini/4o)  (Sandbox)
```

---

## 🚀 Quick Start & Installation

### Prerequisites
- Python 3.10+ (Tested on Python 3.11, 3.12, 3.13)
- Google Gemini API Key (100% Free from [Google AI Studio](https://aistudio.google.com/app/apikey)) **OR** OpenAI API Key

### 1. Clone the Repository
```bash
git clone https://github.com/hasibur-rhman/KrishiMitro.git
cd KrishiMitro
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project root:
```bash
cp .env.example .env
```
Edit `.env` and specify your credentials:
```env
# Option A: 100% Free with Google Gemini (Recommended)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash

# Option B: OpenAI (Optional - Paid)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

# Optional: bdapps credentials for live telco billing (Leave empty for local simulation)
BDAPPS_APP_ID=
BDAPPS_PASSWORD=
BDAPPS_BASE_URL=https://developer.bdapps.com
```

### 4. Build Knowledge Base (ChromaDB)
Ingest the 19 agricultural reference documents into ChromaDB:
```bash
cd backend
python -m app.rag.ingest
```

### 5. Launch the Application
```bash
uvicorn app.main:app --reload --port 8000
```
Access the application at **http://localhost:8000** in your browser.

---

## 🧪 Automated Testing & Quality Assurance

All deterministic mathematical and agronomic calculation engines are protected by automated test suites:
```bash
pytest backend/tests/ -v
```
Test coverage spans:
- `test_finance.py`: Arithmetic consistency, ROI scaling, and budget constraint validations
- `test_pest.py`: Weather and phenology-driven pest risk matrices
- `test_season_plan.py`: Chronological timeline validation from sowing to harvest
- `test_soilmap.py`: Geospatial nearest-neighbor raster interpolation
- `test_awdmap.py`: Alternate Wetting and Drying rice irrigation suitability
- `test_alerts.py`: Weather-triggered schedule adjustments and threshold alarms

---

## 📂 Repository Structure

```
KrishiMitro/
├── backend/
│   ├── app/
│   │   ├── agent/           # Multi-step agent loop, tool dispatch & system prompts
│   │   ├── rag/             # ChromaDB vector store & document ingestion pipeline
│   │   ├── tools/           # Weather, GIS soil/AWD, vision, finance, pest, bdapps
│   │   ├── db.py            # SQLite persistent session & farm profile repository
│   │   ├── config.py        # Environment variables & runtime constants
│   │   └── main.py          # FastAPI application & NDJSON streaming endpoints
│   ├── data/
│   │   ├── kb/              # 19 curated markdown agronomy guides (BARC, BRRI, SRDI, DAM)
│   │   ├── soil_grid.json   # Pre-baked SRDI soil texture raster
│   │   ├── awd_grid.json    # Pre-baked BRRI/IRRI AWD suitability grid
│   │   └── *.json           # Reference crops, livestock, pests, and input prices
│   ├── data_prep/           # Offline raster baking scripts (GeoTIFF -> compact JSON)
│   ├── tests/               # Pytest automated test suites (67 test cases)
│   └── requirements.txt     # Python backend dependencies
├── frontend/
│   ├── index.html           # Farmer chat interface & Live Agent Trace panel
│   ├── app.js               # Reactive client-side logic & NDJSON stream reader
│   └── style.css            # Responsive styles for mobile & desktop
├── pdfs/
│   └── extraction_prompts/  # Prompts used for systematic document extractions
├── Dockerfile               # Production container image configuration
├── HOW_IT_WORKS.md          # Technical architecture & engineering deep-dive
├── DEMO.md                  # Demonstration script & investor pitch playbook
└── README.md                # Project documentation
```

---

## 🤝 Institutional Data Sources & Acknowledgments

This platform synthesizes empirical agronomic research and guidelines from leading national and international bodies:
- **BARC** — Bangladesh Agricultural Research Council (*Fertilizer Recommendation Guide 2024*)
- **BRRI** — Bangladesh Rice Research Institute (*Modern Rice Cultivation Guidelines*)
- **SRDI** — Soil Resource Development Institute (*Soil Fertility Atlas & Soil Texture Rasters*)
- **DAE** — Department of Agricultural Extension (*Agromet Advisory & Plant Protection*)
- **DAM** — Department of Agricultural Marketing (*Division-wise Retail Commodity Pricing*)
- **BBS** — Bangladesh Bureau of Statistics (*Agricultural Yield Statistics*)
- **IRRI** — International Rice Research Institute (*Alternate Wetting and Drying Mapping*)
- **DLS / BLRI** — Department of Livestock Services & Bangladesh Livestock Research Institute
- **Open-Meteo** — High-precision meteorological forecasting API
- **bdapps** — Robi Axiata Telco Application Proxy

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE).  
Engineered with precision for the empowerment of smallholder farmers.
