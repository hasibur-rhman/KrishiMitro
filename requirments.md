# 🌾 KrishiMitro (Fosholer Chikitsha) — Product Specifications & Architecture Matrix

This document outlines the functional and non-functional requirements, technical specifications, and development roadmap for the **KrishiMitro — Fosholer Chikitsha** autonomous agricultural advisory platform.

---

## 📊 Feature Completion & Verification Matrix

### Core Tier 0 Capabilities (Baseline Foundation)

| ID | Requirement Specification | Architectural Implementation | Verification Method | Status |
|---|---|---|---|---|
| **REQ-01** | Conversational Intake & Intelligent Profiling | Adaptive intake protocol in `backend/app/agent/prompts.py`; persists parameters to SQLite via `save_farm_profile`. | Verified with incomplete prompts; tests show agent infers soil and missing fields dynamically. | ✅ Complete |
| **REQ-02** | Real-Time Meteorological Grounding | Open-Meteo REST integration in `backend/app/tools/weather.py` with automated disk caching. | Live API calls verified; temperature and rainfall metrics exposed in trace. | ✅ Complete |
| **REQ-03** | Multi-Crop Comparative Ranking | Ranked analysis of $\ge 3$ candidate crops evaluating soil suitability, water requirements, and risk level. | Tested against diverse agro-ecological profiles; integrates `compute_financials` per candidate. | ✅ Complete |
| **REQ-04** | Validated Phenological Season Calendar | Deterministic `generate_season_plan` in `backend/app/tools/season_plan.py` calculating chronological timelines. | Validated via 9 unit tests in `backend/tests/test_season_plan.py`. | ✅ Complete |
| **REQ-05** | Deterministic Farm Financial Modeling | Algorithmic financial engine in `backend/app/tools/finance.py` calculating cost, yield, gross revenue, net margin, and break-even. | Validated via 10 unit tests in `backend/tests/test_finance.py`. | ✅ Complete |
| **REQ-06** | Grounded Decision Explainability | System prompt rules mandate citing specific weather, soil, and document sources for all advice. | Output traces audited; citations tied directly to institutional sources. | ✅ Complete |
| **REQ-07** | RAG Institutional Knowledge Base | ChromaDB persistent vector repository over 19 verified government manuals (195 indexed chunks). | Semantic search validated via `backend/app/rag/store.py`. | ✅ Complete |
| **REQ-08** | Real-Time Decision Observability (XAI) | Live NDJSON event stream surfacing tool names, parameters, execution latencies, and raw responses. | Verified in UI right-hand inspection panel. | ✅ Complete |

---

### Tier 1 Advanced Capabilities (Differentiators)

| ID | Requirement Specification | Architectural Implementation | Verification Method | Status |
|---|---|---|---|---|
| **REQ-09** | Persistent Cross-Session Memory | Relational storage in SQLite (`farms`, `messages`, `plans` tables) indexed by session identifier. | Verified across server restarts and browser reloads. | ✅ Complete |
| **REQ-10** | Proactive Weather Risk Alerting | Polling endpoint `/api/alerts/{session_id}` correlating 14-day forecasts with planned field operations. | Automated alert banner displays warnings without requiring a chat turn. | ✅ Complete |
| **REQ-11** | Pest & Disease Outbreak Risk Matrix | Weather- and stage-based scoring in `backend/app/tools/pest.py` calculating risk levels and treatment costs. | Validated via 8 unit tests in `backend/tests/test_pest.py`. | ✅ Complete |
| **REQ-12** | Sensitivity & Scenario Modeling ("What-If") | Dynamic overrides in financial engines (`yield_factor`, `cost_factor`, `price_factor`). | Verified across rainfall drop, price collapse, and budget constraint scenarios. | ✅ Complete |
| **REQ-13** | Comprehensive Livestock Parity | Algorithmic financial and vaccination planning for cattle, poultry, and goats (`livestock.py`). | Validated via 13 unit tests in `backend/tests/test_livestock.py`. | ✅ Complete |

---

### Tier 2 Ecosystem & Commercial Integration

| ID | Requirement Specification | Architectural Implementation | Verification Method | Status |
|---|---|---|---|---|
| **REQ-14** | Multimodal Leaf Disease Diagnostics | Computer vision pathology pipeline in `backend/app/tools/vision.py` supporting `gemini-3.8-flash` and `gpt-4o-mini`. | Verified with leaf photo uploads; extracts pathogen and recommends treatment. | ✅ Complete |
| **REQ-15** | Geospatial Soil Texture Interpolation | Pre-baked SRDI rasters in `soil_grid.json` with USDA texture triangle classification in `soilmap.py`. | Validated via 6 unit tests in `backend/tests/test_soilmap.py`. | ✅ Complete |
| **REQ-16** | Alternate Wetting and Drying (AWD) Mapping | Pre-baked BRRI/IRRI rasters in `awd_grid.json` evaluating water-saving rice cultivation suitability. | Validated via 5 unit tests in `backend/tests/test_awdmap.py`. | ✅ Complete |
| **REQ-17** | Market Price Intelligence & Storage Advice | Sinusoidal seasonal price modeling factoring in storage costs and monthly spoilage in `market_intel.py`. | Validated via 10 unit tests in `backend/tests/test_market_intel.py`. | ✅ Complete |
| **REQ-18** | Supplier Marketplace Ranking | Multi-criteria dealer ranking by price, distance, rating, and delivery time in `suppliers.py`. | Validated via unit tests with seeded merchant catalogs. | ✅ Complete |
| **REQ-19** | Telco Direct Carrier Billing & SMS Receipts | CaaS direct-debit and SMS gateway integration via the Robi/Axiata bdapps API specification (`bdapps.py`). | Verified with sandbox endpoints and automated simulation fallback. | ✅ Complete |
| **REQ-20** | Right to be Forgotten (Data Privacy) | Confirm-gated `clear_farm_data` tool providing full data deletion across sessions. | Verified with confirmation validation; wipes SQLite records cleanly. | ✅ Complete |

---

## 📈 Engineering Roadmap & Strategic Objectives

```
[Phase 1: Foundation] ✅ COMPLETE
 ├── Agentic tool-calling architecture & live trace UI
 ├── RAG vector store over 19 national agricultural guides
 ├── Deterministic financial, season-plan, and pest scoring engines
 └── Offline geospatial baking for soil and AWD grids

[Phase 2: Multimodal & Accessibility] ✅ COMPLETE
 ├── Multimodal computer vision leaf disease diagnosis
 ├── 100% Free Google Gemini 3.8 Flash inference integration
 ├── Proactive weather alerting banner
 └── Telco mobile balance micro-payments (bdapps)

[Phase 3: Production & Edge Scaling] 🚀 IN PROGRESS
 ├── Offline Edge Vision Classification (ONNX / TFLite on-device models)
 ├── Multilingual Bengali Speech-to-Speech (Whisper + Bangla TTS)
 ├── Enterprise Hybrid Search (Dense Chroma + Sparse BM25 Reranking)
 └── Continuous Evaluation Pipeline (Ragas & LLM automated benchmarks)
```
