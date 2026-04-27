# 🕵️ Competitor Intel Crew

> An automated multi-agent AI system that researches competitors, analyzes sentiment, and generates professional market intelligence reports — powered by CrewAI and local LLMs via Ollama.

---

## 📌 Overview

**Competitor Intel Crew** is a production-ready multi-agent system built with the [CrewAI](https://docs.crewai.com) framework. It automates the entire competitor research pipeline for Indian D2C brands and e-commerce sellers on Amazon India and Flipkart.

Instead of spending 10–20 hours per week manually tracking competitor pricing, reviews, and promotions — run one command and get a full intelligence report in minutes.

---

## 🎯 Problem It Solves

Small and medium businesses in India's competitive D2C and e-commerce space (Amazon, Flipkart, Meesho) manually track:

- Competitor pricing and promotions
- New product launches
- Customer reviews and sentiment shifts
- Marketing strategies

This process is **time-consuming, inconsistent, and leads to delayed decisions**. This system automates all of it.

---

## 🤖 Agent Architecture

Five specialized AI agents work sequentially, each passing context to the next:

| Agent | Role | Tools |
|---|---|---|
| 🔍 Web Researcher | Finds real-time pricing, products, and promotions | SerperDevTool |
| 💬 Sentiment Analyst | Analyzes customer reviews per brand | Custom BS4 Scraper |
| 📊 Competitor Analyst | Builds comparison tables, identifies market gaps | — |
| 🧠 Strategy Generator | Generates ranked actionable recommendations | — |
| 📝 Report Writer | Writes professional markdown report to disk | FileWriterTool |

---

## 🗂️ Project Structure

```
competitor_intel_crew/
├── src/competitor_intelligence/
│   ├── config/
│   │   ├── agents.yaml          # Agent roles, goals, backstories
│   │   └── tasks.yaml           # Task descriptions, expected outputs
│   ├── tools/
│   │   ├── search_tool.py           # SerperDevTool wrapper
│   │   ├── scrape_tool.py           # ScrapeWebsiteTool wrapper
│   │   ├── sentiment_scrape_tool.py # Custom BeautifulSoup review scraper
│   │   ├── file_writer_tool.py      # FileWriterTool locked to /output
│   │   ├── file_read_tool.py        # FileReadTool
│   │   └── __init__.py
│   ├── crew.py                  # Agent + task definitions
│   └── main.py                  # Entry point
├── output/                      # Generated reports land here
├── .env.example                 # Required environment variables
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## ⚙️ Tech Stack

- **[CrewAI](https://docs.crewai.com)** — Multi-agent orchestration framework
- **[Ollama](https://ollama.com)** — Local LLM inference (no API costs)
- **[Mistral-Nemo 12B](https://ollama.com/library/mistral-nemo)** — Primary LLM running on GPU
- **[Serper API](https://serper.dev)** — Real-time Google Search
- **BeautifulSoup4** — Custom review scraper targeting Amazon's `data-hook="review"` attributes
- **Pydantic** — Structured data validation
- **LiteLLM** — LLM provider routing

---

## 🖥️ Hardware Requirements

Tested on:
- GPU: NVIDIA RTX 4060 8GB VRAM
- RAM: 16 GB
- OS: Windows 11
- Python: 3.11

The `mistral-nemo:12b` model uses ~7.1GB VRAM and runs fully on GPU.

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.11
- [Ollama](https://ollama.com/download) installed
- [Serper API key](https://serper.dev) (free tier: 2,500 searches/month)

### 2. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/competitor-intel-crew.git
cd competitor-intel-crew
```

### 3. Install dependencies

```bash
pip install crewai crewai-tools 'crewai[litellm]' beautifulsoup4 requests python-dotenv
```

Or with uv:
```bash
uv sync
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your keys:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_HOST=http://localhost:11434
SERPER_API_KEY=your_serper_key_here
```

### 5. Pull the LLM and embedding model

```bash
ollama pull mistral-nemo:12b
ollama pull nomic-embed-text
```

### 6. Start Ollama server (keep this terminal open)

```bash
ollama serve
```

### 7. Run the crew

```bash
crewai run
```

---

## 📊 Example Output

**Input:**
```
Market: Mumbai ready-to-eat healthy snacks market
Competitors: EatFit, Slurrp Farm
```

**Output** (`output/intelligence_report.md`):

```
EXECUTIVE SUMMARY
EatFit leads with protein-rich snacks and higher review counts.
SlurrpFarm offers unique value in whole grains and smoothie mixes...

KEY FINDINGS
- Market Leader: EatFit (2,119+ reviews, 4.3/5 avg rating)
- Market Gaps: Gluten-free options, vegan-specific lines

RANKED RECOMMENDATIONS
1. Product Expansion into Vegan-specific Lines (High Impact)
2. Improve Launch Promotions (Medium Impact)
...
```

---

## 🔧 Customization

Change the market and competitors in `main.py`:

```python
result = CompetitorIntelligence().crew().kickoff(inputs={
    "market": "Delhi electronics market",
    "competitors": "Boat, Noise, Fire-Boltt",
})
```

---

## 🌐 Supported Markets

The system works for any Indian market segment:

- 🍎 Food & Snacks (D2C brands)
- 👗 Fashion & Apparel
- 📱 Electronics & Accessories
- 💄 Beauty & Personal Care
- 🏋️ Health & Fitness

---

## 📄 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `OLLAMA_BASE_URL` | Ollama server URL | ✅ |
| `OLLAMA_HOST` | Ollama host | ✅ |
| `SERPER_API_KEY` | Google Search API key | ✅ |
| `FIRECRAWL_API_KEY` | Firecrawl scraping (optional) | ❌ |

---

## 🤝 Use Cases

- E-commerce sellers tracking competitors weekly
- D2C founders monitoring market positioning
- Marketing teams automating competitive research
- Business consultants generating client reports

---

## 📝 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author

Built by **Nirlep Sanap**

> *"Automate the boring research. Focus on the strategy."*
