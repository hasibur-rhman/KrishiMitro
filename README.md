# 🌾 KrishiMitro — ফসলের চিকিৎসা (Fosholer Chikitsha)
### *AI-Powered Digital Crop Doctor & Autonomous Agricultural Advisory Platform*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Google_Gemini-3.8_Flash_(Free)-8E75C2.svg?logo=google&logoColor=white)](https://aistudio.google.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-Supported-412991.svg?logo=openai&logoColor=white)](https://platform.openai.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-orange.svg)](https://www.trychroma.com)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![Platform](https://img.shields.io/badge/Startup-Fosholer_Chikitsha-brightgreen.svg)](https://fosholerchikitsha.com)

---

## 📖 About the Platform

**KrishiMitro — ফসলের চিকিৎসা (Fosholer Chikitsha)** is an intelligent, autonomous agronomic advisory and digital doctor platform engineered for smallholder farmers in Bangladesh. Designed to support the vision of **ফসলের চিকিৎসা (Fosholer Chikitsha)** ([fosholerchikitsha.com](https://fosholerchikitsha.com/)), this platform bridges the gap between agricultural research institutions and grassroots farmers.

The system combines **Agentic AI (multi-step tool orchestration)**, **Multimodal Computer Vision (leaf disease diagnosis)**, **Retrieval-Augmented Generation (RAG over verified government agronomy manuals)**, and **Deterministic Algorithmic Engines** to provide trustworthy, zero-hallucination guidance.

---

## ✨ Core Pillars & Capabilities

### 1. 🩺 ফসলের রোগ নির্ণয় (AI Leaf Disease Diagnosis)
- Farmers can capture or upload photos of affected leaves directly from the field.
- Multimodal Vision AI (`gemini-3.8-flash` / `gpt-4o-mini`) inspects physical leaf symptoms (lesions, discoloration, fungal spots), detects the disease or pest in both English and Bengali, and estimates confidence.
- Diagnosis is cross-verified against the vetted **Integrated Pest Management (IPM)** knowledge base for recommended chemical/organic remedies.

### 2. 🐛 পোকামাকড় ও বালাই পূর্বাভাস (Pest & Disease Risk Engine)
- Deterministic scoring engine calculates pest outbreak risks based on real-time weather (temperature, humidity, recent rainfall from Open-Meteo) and current crop phenological stage (seedling, tillering, flowering, bulking).
- Recommends proactive preventive measures and cost-effective treatments.

### 3. 📅 আবহাওয়া-সচেতন সিজনাল ক্যালেন্ডার (Weather-Aware Season Plan)
- Generates a dated, chronologically validated crop calendar from land preparation to harvest.
- Integrates fertilizer application stages, weeding intervals, and irrigation checkpoints.
- **Proactive Alerts:** Watches the 14-day weather forecast against planned dates (e.g., delaying urea top-dressing if heavy rain is incoming).

### 4. 🗺️ ভূ-স্থানিক মাটি ও AWD বিশ্লেষণ (Geospatial Soil & Irrigation)
- **Soil Texture Auto-Detection:** Maps farm GPS coordinates against SRDI (Soil Resource Development Institute) rasters to detect clay/sand/silt percentages and USDA soil classification.
- **AWD (Alternate Wetting and Drying) Suitability:** Samples BRRI/IRRI spatial suitability maps to identify water-saving rice cultivation zones, cutting irrigation costs by 25–30%.

### 5. 💰 আর্থিক প্রজেকশন ও সিনারিও মডেলিং (Deterministic Financial Engine)
- Zero-hallucination financial modeling in pure Python: itemized input costs (seeds, fertilizers, labor, pesticides, irrigation), expected yield, revenue, net profit, ROI, and break-even point.
- **Scenario Simulation ("What-If"):** Adjusts forecasts dynamically based on price fluctuations, budget restrictions, or climate changes (`yield_factor`, `cost_factor`, `price_factor`).

### 6. 📚 RAG Knowledge Base (Government Agronomy Grounding)
- ChromaDB vector store indexed over **19 verified public documents & manuals**:
  - **BARC:** Fertilizer Recommendation Guide (FRG 2024)
  - **BRRI:** Modern Rice Cultivation Guidelines & Varieties
  - **SRDI:** Soil Fertility Atlas 2020 & Soil Maps
  - **DAE:** Agromet Advisory Bulletins & Plant Protection Manuals
  - **BBS:** Agricultural Yield Statistics 2024
  - **DAM:** Department of Agricultural Marketing division-wise retail price reports (Dhaka, Chattogram, Rajshahi, Khulna, Barishal, Sylhet, Rangpur, Mymensingh)
  - **DLS / BLRI:** Livestock management and vaccination guides

### 7. 📲 টেলকো পেমেন্ট ও এসএমএস নোটিফিকেশন (bdapps Integration)
- Full **Charging-as-a-Service (CaaS)** and **SMS API** workflow via the bdapps platform.
- Farmers can purchase agricultural inputs via mobile account balance deduction and receive SMS invoices and urgent weather warnings.

### 8. 🔍 সম্পূর্ণ স্বচ্ছ এজেন্ট ট্রেস (Live Agent Trace / Explainable AI)
- Every single tool call, coordinate lookup, weather API query, RAG retrieval chunk, and financial formula calculation is streamed live via NDJSON in the right-hand inspection panel.

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
  (Open-Meteo) (19 Docs) (Finance/Pest)  (Soil/AWD)   (4o-mini)   (Sandbox)
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
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```
Edit `.env` and insert your credentials:
```env
# Option A: 100% Free with Google Gemini (Recommended)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash

# Option B: OpenAI (Optional - Paid)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini

# Optional: bdapps credentials for live telco billing (Leave empty for built-in simulation)
BDAPPS_APP_ID=
BDAPPS_PASSWORD=
BDAPPS_BASE_URL=https://developer.bdapps.com
```

### 4. Build Knowledge Base (ChromaDB)
Ingest the 19 agricultural source documents into ChromaDB:
```bash
cd backend
python -m app.rag.ingest
```

### 5. Launch the Application
```bash
uvicorn app.main:app --reload --port 8000
```
Open **http://localhost:8000** in your browser.

---

## 🧪 Testing & Verification

The deterministic calculation engines come with comprehensive unit tests:
```bash
cd backend
pytest tests/ -v
```
Test suites cover:
- `test_finance.py`: Financial consistency, ROI scaling, and budget limits
- `test_pest.py`: Weather and phenology-driven pest risk matrices
- `test_season_plan.py`: Chronological timeline validation
- `test_soilmap.py`: Geospatial nearest-neighbor lookup
- `test_awdmap.py`: Alternate Wetting and Drying suitability
- `test_alerts.py`: Weather-triggered schedule adjustments

---

## 📂 Repository Structure

```
KrishiMitro/
├── backend/
│   ├── app/
│   │   ├── agent/           # Multi-step agent loop, tool dispatch & prompts
│   │   ├── rag/             # ChromaDB vector store & ingestion pipeline
│   │   ├── tools/           # Weather, GIS soil/AWD, vision, finance, pest, bdapps
│   │   ├── db.py            # SQLite persistent session & farm profile store
│   │   ├── config.py        # Environment variables & constants
│   │   └── main.py          # FastAPI application & NDJSON streaming endpoints
│   ├── data/
│   │   ├── kb/              # 19 curated markdown agronomy guides (BARC, BRRI, SRDI, DAM)
│   │   ├── soil_grid.json   # Pre-baked SRDI soil texture raster
│   │   ├── awd_grid.json    # Pre-baked BRRI/IRRI AWD suitability grid
│   │   └── *.json           # Seeded crops, livestock, pests, and input prices
│   ├── data_prep/           # Offline raster baking scripts (GeoTIFF -> compact JSON)
│   ├── tests/               # Pytest automated test suites
│   └── requirements.txt     # Python backend dependencies
├── frontend/
│   ├── index.html           # Farmer chat interface & Live Agent Trace panel
│   ├── app.js               # Reactive client-side logic & NDJSON stream reader
│   └── style.css            # Responsive styles for mobile & desktop
├── pdfs/
│   └── extraction_prompts/  # Prompts used for systematic document extractions
├── HOW_IT_WORKS.md          # Technical deep-dive & architectural decisions
└── README.md                # Project documentation
```

---

## 🤝 Acknowledgments & Sources
This project builds on agricultural data and guidelines published by:
- **BARC** (Bangladesh Agricultural Research Council)
- **BRRI** (Bangladesh Rice Research Institute)
- **SRDI** (Soil Resource Development Institute)
- **DAE** (Department of Agricultural Extension)
- **DAM** (Department of Agricultural Marketing)
- **BBS** (Bangladesh Bureau of Statistics)
- **DLS / BLRI** (Department of Livestock Services & Bangladesh Livestock Research Institute)
- **Open-Meteo** (Free Meteorological API)
- **bdapps** (Robi Axiata Telco Application Proxy)

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE).
Developed with ❤️ for the farmers of Bangladesh.
