# 🕵️ Competitor Intel Crew

> Paste one command. Get a full competitor intelligence report in minutes.

---

## 📌 The Problem

Every week, business owners manually check:
- What are competitors charging on Amazon and Flipkart?
- What are customers complaining about?
- Who is winning — and why?

This takes **10–20 hours per week**. This project does it automatically.

---

## ✅ The Solution

An AI system made of **5 agents** that work as a team:

| Step | Agent | What it does |
|---|---|---|
| 1 | 🔍 Web Researcher | Searches Amazon India & Flipkart for live prices and products |
| 2 | 💬 Sentiment Analyst | Reads customer reviews and finds what people love or hate |
| 3 | 📊 Competitor Analyst | Compares brands side by side |
| 4 | 🧠 Strategy Consultant | Turns data into 5 ranked business recommendations |
| 5 | 📝 Report Writer | Writes the final professional report and saves it |

---

## 🔄 Detailed Project Flow

Here is exactly what happens when you run `crewai run`:

```
YOU
 │
 ▼
┌─────────────────────────────────────────────┐
│  main.py                                    │
│  Reads: market + competitors from inputs    │
│  Kicks off the 5-agent crew                 │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  AGENT 1 — 🔍 Web Researcher                │
│                                             │
│  Tool used: Serper API (Google Search)      │
│                                             │
│  → Searches "EatFit Amazon India prices"    │
│  → Searches "Slurrp Farm Flipkart products" │
│  → Extracts: product names, prices,         │
│    ratings, promotions, new launches        │
│                                             │
│  Output: Structured product data list       │
└─────────────────┬───────────────────────────┘
                  │ passes data to ↓
                  ▼
┌─────────────────────────────────────────────┐
│  AGENT 2 — 💬 Sentiment Analyst             │
│                                             │
│  Tool used: Custom BeautifulSoup Scraper    │
│                                             │
│  → Takes product URLs from Agent 1          │
│  → Scrapes Amazon review pages              │
│  → Targets data-hook="review" attributes    │
│  → Strips ads, nav, irrelevant content      │
│  → Identifies top 3 complaints per brand   │
│  → Identifies top 3 praises per brand      │
│                                             │
│  Output: Sentiment summary per brand        │
└─────────────────┬───────────────────────────┘
                  │ passes data to ↓
                  ▼
┌─────────────────────────────────────────────┐
│  AGENT 3 — 📊 Competitor Analyst            │
│                                             │
│  Tool used: None (pure reasoning)           │
│                                             │
│  → Receives data from Agent 1 + Agent 2    │
│  → Builds side-by-side comparison table    │
│  → Identifies the market leader            │
│  → Spots 2-3 unserved market gaps          │
│                                             │
│  Output: Comparison table + written         │
│          analysis                           │
└─────────────────┬───────────────────────────┘
                  │ passes data to ↓
                  ▼
┌─────────────────────────────────────────────┐
│  AGENT 4 — 🧠 Strategy Consultant           │
│                                             │
│  Tool used: None (pure reasoning)           │
│                                             │
│  → Receives analysis from Agent 3          │
│  → Generates 5 specific recommendations   │
│  → Ranks each by Impact: High/Medium/Low   │
│  → Ranks each by Effort: High/Medium/Low   │
│                                             │
│  Output: Ranked recommendation list        │
└─────────────────┬───────────────────────────┘
                  │ passes data to ↓
                  ▼
┌─────────────────────────────────────────────┐
│  AGENT 5 — 📝 Report Writer                 │
│                                             │
│  Tool used: FileWriterTool                  │
│                                             │
│  → Receives all outputs from Agents 1-4   │
│  → Writes clean professional Markdown      │
│  → Saves to output/intelligence_report.md  │
│                                             │
│  Output: Final report file on your disk    │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
         📄 intelligence_report.md
         Ready to read, share, or present
```

**Key design decisions:**
- Each agent only receives context it needs — no bloated prompts
- Serper API returns clean snippets — no full page scraping for research
- Custom scraper only activates for review pages — targeted and fast
- All agents run on local GPU via Ollama — zero data sent to cloud
- Sequential process ensures each agent builds on verified prior output

---

## 📋 Sample Output

**You type:**
```
Market: Mumbai ready-to-eat healthy snacks
Competitors: EatFit, Slurrp Farm
```

**You get** `output/intelligence_report.md` containing:

```
EXECUTIVE SUMMARY
EatFit leads with protein-rich snacks and 2,100+ reviews.
Slurrp Farm offers unique value in whole grains and smoothie mixes...

KEY FINDINGS
- Market Leader: EatFit (4.3/5 avg rating, aggressive promotions)
- Market Gap: No brand targeting gluten-free or vegan customers

RANKED RECOMMENDATIONS
1. Launch vegan-specific product line (High Impact, Medium Effort)
2. Offer bundle discounts to compete with SlurrpFarm pricing
...
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [CrewAI](https://docs.crewai.com) | Coordinates the 5 AI agents |
| [Ollama](https://ollama.com) | Runs AI locally on your GPU — no cloud needed |
| [Qwen 2.5 7B](https://ollama.com/library/qwen2.5) | The AI model powering all agents |
| [Serper API](https://serper.dev) | Real-time Google search |
| BeautifulSoup4 | Scrapes Amazon customer reviews |
| Python 3.11 | Core language |

---

## 💻 Requirements

- Python 3.11
- NVIDIA GPU with 6GB+ VRAM (tested on RTX 4060 8GB)
- [Ollama](https://ollama.com/download) installed
- Free [Serper API key](https://serper.dev) (2,500 searches/month free)

---

## 🚀 Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/competitor-intel-crew.git
cd competitor-intel-crew
```

**2. Install dependencies**
```bash
pip install crewai crewai-tools 'crewai[litellm]' beautifulsoup4 requests python-dotenv ollama
```

**3. Set up your API keys**
```bash
cp .env.example .env
```

Edit `.env`:
```env
OLLAMA_BASE_URL=http://localhost:11434
SERPER_API_KEY=your_key_here
```

**4. Pull the AI model**
```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

**5. Start Ollama (keep this terminal open)**
```bash
ollama serve
```

**6. Run the crew (new terminal)**
```bash
crewai run
```

**7. Find your report at:**
```
output/intelligence_report.md
```

---

## ⚙️ Customize for Your Market

Open `main.py` and change these two lines:

```python
inputs = {
    "market": "Delhi electronics market",        # ← your market
    "competitors": "Boat, Noise, Fire-Boltt",    # ← your competitors
}
```

Works for any Indian market — food, fashion, electronics, beauty, fitness.

---

## 📁 Project Structure

```
competitor-intel-crew/
├── src/competitor_intelligence/
│   ├── config/
│   │   ├── agents.yaml          # What each agent knows and does
│   │   └── tasks.yaml           # What each agent is asked to do
│   ├── tools/
│   │   ├── search_tool.py           # Google search via Serper
│   │   ├── sentiment_scrape_tool.py # Custom Amazon review scraper
│   │   ├── file_writer_tool.py      # Saves the final report
│   │   └── __init__.py
│   ├── crew.py                  # Agent and task definitions
│   └── main.py                  # Entry point
├── output/                      # Reports saved here
├── .env.example                 # Required environment variables
├── pyproject.toml
└── README.md
```

---

## 🔒 Security

- API keys stored in `.env` — never hardcoded
- `.env` in `.gitignore` — never pushed to GitHub
- AI runs locally via Ollama — your data never leaves your machine

---

## 👤 Author

**Nirlep Sanap**

> Built to solve a real problem — manual competitor research is broken. This fixes it.

---

## ⭐ If this helped you

Give it a star on GitHub — it helps others find this project.
