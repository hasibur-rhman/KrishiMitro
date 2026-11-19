# 🌾 KrishiMitro (Fosholer Chikitsha) — Technical Architecture & System Design

## 📌 Executive Summary
**KrishiMitro — Fosholer Chikitsha** is an autonomous agronomic agent that guides smallholder farmers from field preparation to harvest with **weather-aware, economically optimized crop planning**. Unlike conventional chatbots that answer isolated questions, this platform chains dependent reasoning tools, retrieves empirical agronomic data from institutional RAG knowledge bases, computes economics deterministically, and provides complete decision explainability via a real-time event trace.

---

## 🛠️ Technology Stack & Architectural Justifications

| Architectural Layer | Technology Selected | Engineering Rationale |
|---|---|---|
| **Cognitive Brain** | **Google Gemini (`gemini-3.8-flash`) / OpenAI GPT-4o** | High-speed multi-step tool-calling with low latency and native multimodal vision capabilities. |
| **Application Server** | **Python + FastAPI + Uvicorn** | Asynchronous request processing, native NDJSON event streaming, and integrated static asset serving. |
| **Vector Database (RAG)** | **ChromaDB (Embedded Persistent Client)** | Zero-latency local vector similarity search over 19 verified agricultural manuals with zero cloud DB overhead. |
| **Session Persistence** | **SQLite (WAL mode enabled)** | Persistent local relational storage for farm profiles, conversation history, and crop calendars across sessions. |
| **Frontend Interface** | **Vanilla HTML5 / Modern CSS / JavaScript** | Ultra-lightweight footprint optimized for rural bandwidth; zero bundle build overhead or framework bloat. |
| **Meteorological Engine** | **Open-Meteo REST API** | Live, keyless meteorological forecasting with automated fallback caching against network disruptions. |
| **Payment Gateway** | **bdapps Telco Application Proxy (CaaS / SMS)** | Native direct carrier billing via mobile airtime deduction and transactional SMS receipt generation. |
| **Web Retrieval Fallback** | **DuckDuckGo Search (`ddgs`)** | Real-time fallback for emerging commodity market prices, auto-cataloging verified findings back into ChromaDB. |
| **Geospatial Processing** | **Offline Raster Baking (`rasterio` $\rightarrow$ JSON Grid)** | Eliminates heavy C-extensions in production by precomputing GIS rasters into spatial grid matrices. |

---

## 🧠 Architectural Philosophy: Agent vs. Chatbot

A standard conversational chatbot answers single questions using internalized weights, creating high susceptibility to numerical hallucinations. 

In contrast, **KrishiMitro operates as an Autonomous Goal-Seeking Agent**:
1. **Multi-Turn Decomposition:** A single prompt like *"I have 2 acres in Bogura with an 80k budget"* automatically initiates a sequence of 6+ dependent tool calls:
   `geocode_location` $\rightarrow$ `lookup_soil_texture` $\rightarrow$ `get_weather_forecast` $\rightarrow$ `search_knowledge_base` $\rightarrow$ `compute_financials (x3 candidates)` $\rightarrow$ synthesis.
2. **Deterministic Arithmetic Boundary:** The LLM is strictly prohibited from calculating currency, yield projections, fertilizer proportions, or dates. All arithmetic is delegated to pure Python mathematical engines.
3. **Observability & Auditability (XAI):** Every tool invocation, parameter dictionary, execution time (in milliseconds), and raw JSON payload is streamed live to the UI's **Agent Trace Panel**.

---

## 🔄 End-to-End Request Lifecycle

```
Farmer Input (Web UI)
        │
        ▼
FastAPI `/api/chat` Route
        │
        ▼
Orchestration Loop (`loop.py`)
  ├── Appends message to SQLite message history
  ├── Loads persistent farm profile from SQLite
  ├── Synthesizes dynamic system prompt with grounded context
  └── Invokes LLM with registered OpenAI-format tool schemas
        │
        ▼
Tool Execution & Dispatch (`tools.py`)
  ├── Executes required tool functions (Weather / Soil / RAG / Finance)
  ├── Logs execution duration (ms)
  └── Streams events via NDJSON (`tool_call`, `tool_result`, `final`)
        │
        ▼
UI Client Stream Reader (`app.js`)
  ├── Renders conversational dialogue in Chat Panel
  └── Renders expandable JSON inspection tree in Live Trace Panel
```

---

## 🧰 Integrated Toolset Registry (21 Capabilities)

### 1. Grounding & Geospatial Intelligence
- `geocode_location`: Resolves administrative names into WGS84 GPS coordinates.
- `get_weather_forecast`: Retrieves 14-day rainfall probability, temperature range, and humidity.
- `lookup_soil_texture`: Samples SRDI digital soil rasters to classify sand/silt/clay fractions and USDA soil classes.
- `lookup_awd_suitability`: Evaluates BRRI/IRRI spatial rasters for Alternate Wetting & Drying water savings.
- `search_knowledge_base`: Semantic vector retrieval across 19 public agronomy research documents.
- `web_search`: Dynamic search fallback that auto-indexes unverified findings for future queries.

### 2. Deterministic Mathematical Engines
- `compute_financials`: Itemized expenditure, yield estimates, gross revenue, net margin, and break-even analysis.
- `generate_season_plan`: Validates and schedules a complete calendar from seedbed preparation to harvest.
- `assess_pest_risk`: Multi-factor risk scoring based on growth phenology and weather thresholds.
- `market_price_intelligence`: Sinusoidal commodity price modeling, factoring in storage costs and monthly spoilage rates.
- `compute_livestock_financials` & `generate_livestock_plan`: Financial and vaccination calendar generation for livestock.

### 3. Commerce & Commodity Tools
- `get_market_prices`: Commodity farm-gate and wholesale prices (Department of Agricultural Marketing data).
- `get_input_prices`: Certified input costs for seeds, fertilizers, and plant protection chemicals.
- `compare_suppliers`: Dealer comparison algorithm ranking by price, proximity, delivery time, and customer ratings.

### 4. Vision Diagnostics & Extension Integration
- `diagnose_leaf`: Multimodal vision analysis identifying crop diseases from uploaded field photos.
- `check_weather_alerts`: Background event monitor correlating upcoming weather anomalies with planned field activities.
- `bdapps_checkout` / `bdapps_send_sms`: Automated CaaS mobile charging and SMS delivery workflows.

---

## 📚 Institutional Research Foundations

All agronomic intelligence is compiled from verified public research documents:

| Institution | Institutional Role | Integrated Knowledge Base Assets |
|---|---|---|
| **BARC** | Apex agricultural research coordinator | *Fertilizer Recommendation Guide (FRG 2024)* |
| **BRRI** | National rice research institute | *Modern Rice Cultivation Guidelines* & AWD Suitability Rasters |
| **SRDI** | National soil survey institute | *Soil Fertility Atlas 2020* & Multi-Layer Texture Rasters |
| **DAE** | Agricultural extension department | Agromet Advisory Bulletins & IPM Compendiums |
| **DAM** | Agricultural marketing authority | 8 Regional Market Price Reports (Current, Monthly, and Annual Trends) |
| **BBS** | National statistics bureau | *Yearbook of Agricultural Statistics (2024 Yield Baselines)* |
| **DLS / BLRI** | Livestock research & extension | Rearing guidelines, feed formulations, and vaccination regimens |
| **IRRI** | Global rice research institute | AWD irrigation suitability modeling (with BRRI) |

---

## 🔒 Reliability, Security & Data Privacy

1. **Air-Gapped Math Security:** Even under adversarial prompt injection, the agent cannot invent financial metrics or alter fertilizer safety ceilings.
2. **Right to be Forgotten:** Farmers can request complete data erasure (`clear_farm_data`), which requires explicit confirmation before wiping all session profiles, plans, and conversation histories from SQLite.
3. **Graceful Network Degradation:** Weather and geocoding services automatically fall back to cached payloads if upstream network connectivity is interrupted.
