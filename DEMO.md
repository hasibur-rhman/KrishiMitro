# 🌾 ফসলের চিকিৎসা (KrishiMitro) — Live Demonstration & Pitch Playbook

A structured demonstration walkthrough for **Fosholer Chikitsha (ফসলের চিকিৎসা)**, showcasing the autonomous agent, leaf disease diagnosis, weather-aware season calendar, and financial planning.

---

## ⏱️ Pre-Demo Setup Checklist
- [ ] Dependencies installed: `source .venv/bin/activate`
- [ ] Knowledge base verified: `cd backend && python -m app.rag.ingest` (195 chunks / 19 docs indexed in ChromaDB)
- [ ] Application running: `uvicorn app.main:app --port 8000`
- [ ] Open in browser: **http://localhost:8000**
- [ ] `.env` has valid `GEMINI_API_KEY` (Free) or `OPENAI_API_KEY`
- [ ] Click **"New farm"** to clear session history and start fresh.

---

## 🎤 30-Second Elevator Pitch
> *"ফসলের চিকিৎসা (KrishiMitro) হলো বাংলাদেশের কৃষকদের জন্য একটি এআই-চালিত ডিজিটাল ডাক্তার ও পরামর্শক প্ল্যাটফর্ম। সাধারণ চ্যাটবটের মতো এটি কেবল কথা বলে না, বরং একটি অটোনোমাস এজেন্ট হিসেবে লাইভ আবহাওয়া, সরকারি নলেজ বেস, ভূ-স্থানিক মাটির ডাটা এবং পাইথনের ডিটারমিনিস্টিক আর্থিক ক্যালকুলেশন ব্যবহার করে কৃষকের ফসলের রোগ নির্ণয় ও লাভজনক সিজনাল পরিকল্পনা তৈরি করে দেয়। এর প্রতিটি হিসাব ডানপাশের লাইভ ট্রেস প্যানেলে সম্পূর্ণ স্বচ্ছ ও যাচাইযোগ্য।"*

---

## ▶️ Step-by-Step 4-Minute Demo Script

### 1. Conversational Intake & Geospatial Soil Auto-Detection
- **Farmer Prompt:** *"আমার ২ একর জমি বগুড়ায়, বাজেট ৮০ হাজার টাকা, রবি মৌসুমে কি চাষ করব?"*
- **What to Observe in Live Trace:**
  - `geocode_location` Open-Meteo থেকে GPS স্থানাঙ্ক বের করে।
  - `lookup_soil_texture` SRDI-এর ডিজিটাল সয়েল ম্যাপ থেকে স্বয়ংক্রিয়ভাবে দোআঁশ (Clay Loam) মাটি শনাক্ত করে।
  - `get_weather_forecast` আগামী ১৪ দিনের লাইভ পূর্বাভাস নিয়ে আসে।
  - কৃষককে অতিরিক্ত বিরক্ত না করে প্রয়োজনীয় ৩টি উপযুক্ত ফসলের তুলনামূলক তালিকা উপস্থাপন করে।

### 2. Multi-Crop Ranking with Deterministic Economics
- এজেন্ট ৩টি উপযুক্ত ফসল (যেমন: আলু, গম, সরিষা) সাজিয়ে দেয়।
- প্রতিটি ফসলের পানি চাহিদা, ঝুঁকির মাত্রা, সম্ভাব্য খরচ, ফলন এবং প্রফিট মার্জিন (ROI) হিসাব করে দেয়।

### 3. Crop Selection & Dated Season Calendar
- **Farmer Prompt:** *"আলুর সম্পূর্ণ চাষের রুটিন দাও"*
- **Result:** জমি তৈরি, সার প্রয়োগের কিস্তি (ইউরিয়া, টিএসপি, এমওপি), সেচের দিন এবং ফসল তোলার সুনির্দিষ্ট তারিখসহ একটি ভ্যালিডেটেড ক্যালেন্ডার তৈরি হয়।

### 4. AWD (Alternate Wetting and Drying) Water-Saving Technology
- **Farmer Prompt:** *"সেচ খরচ কমানোর উপায় কি?"*
- **Result:** BRRI/IRRI-এর ভূ-স্থানিক AWD ম্যাপ যাচাই করে ধানের ক্ষেত্রে ২৫-৩০% পানি ও খরচ সাশ্রয়ের বৈজ্ঞানিক গাইডলাইন দেয়।

### 5. AI Leaf Disease Diagnosis (Computer Vision)
- ক্যামেরা আইকন (📷) ক্লিক করে পোকা ধরা বা রোগাক্রান্ত পাতার ছবি আপলোড করুন।
- **Result:** Multimodal Vision AI (`gemini-3.8-flash` / `gpt-4o-mini`) পাতার লক্ষণ বিশ্লেষণ করে রোগের নাম (যেমন: লেট ব্লাইট / ব্লাস্ট), নিশ্চিতের মাত্রা (Confidence) এবং বালাইনাশক স্প্রে করার সঠিক প্রেসক্রিপশন দেয়।

### 6. Proactive Weather Alerts
- উপরে নোটিফিকেশন ব্যানার লক্ষ্য করুন: যদি আগামী কয়েকদিনের মধ্যে ভারী বৃষ্টির সম্ভাবনা থাকে, তবে ইউরিয়া উপরিপ্রয়োগ বা সেচ পিছিয়ে দেওয়ার স্বয়ংক্রিয় সতর্কবার্তা দেখায়।

### 7. Direct Official Helpline Tap-to-Call
- **Farmer Prompt:** *"কৃষি কর্মকর্তার সাথে কথা বলতে চাই"*
- **Result:** স্ক্রিনে সরাসরি কৃষি কল সেন্টারের **📞 ১৬১২৩** ডায়াল বাটন চলে আসে।

### 8. Telco Micro-Payment & SMS Receipt (bdapps)
- প্রয়োজনীয় সার বা বীজ কেনার ক্ষেত্রে মোবাইল ব্যালেন্স থেকে পেমেন্ট ও কনফার্মেশন এসএমএস রিসিটের সম্পূর্ণ সিমুলেশন দেখা যায়।

---

## 🛡️ Key Value Propositions & Answers

| বিষয় | কৃষকের সুবিধা |
|---|---|
| **কোনো অনুমানের হিসাব নেই (Zero Hallucination)** | সমস্ত আর্থিক হিসাব ও সারের ডোজ পাইথনের ডিটারমিনিস্টিক কোডে গণনা করা হয়। |
| **সরকারি গবেষণা তথ্যের ভিত্তি** | BARC, BRRI, SRDI, DAE এবং DAM-এর ১৯টি অফিসিয়াল ম্যানুয়ালের ওপর RAG কাজ করে। |
| **লাইভ আবহাওয়া সচেতনতা** | ওপেন-মেটিও রিয়েল-টাইম এপিআই থেকে বৃষ্টি ও তাপমাত্রার ডাটা নিয়ে পরামর্শ অ্যাডজাস্ট হয়। |
| **স্মার্ট মেমোরি** | ব্রাউজার রিলোড দিলেও SQLite ডাটাবেজ কৃষকের জমির তথ্য ও পূর্বের চ্যাট মনে রাখে। |
