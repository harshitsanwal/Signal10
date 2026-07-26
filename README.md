# 📡 Signal10

Signal10 is a mood-driven news aggregator. Instead of scrolling endless headlines, you tell it how you're feeling on a scale of 1–10, and it fetches real, live news that matches your mood — from light entertainment to serious world events. You can also skip the mood scale entirely and search any topic directly.

---

## 🚀 How It Works

At the core of Signal10 is a simple idea: **not every news story fits every mood.**

- 🎚️ **Rate your day (1–10)** using the slider on the homepage.
  - 😌 **Lower ratings (1–3)** → light, easygoing content — entertainment, celebrity news, feel-good stories, pop culture.
  - ⚖️ **Mid-range ratings (4–7)** → balanced, everyday content — technology, business, general lifestyle, science.
  - 🌍 **Higher ratings (8–10)** → serious, high-impact content — breaking world news, major political developments, global economic updates.
- 🔎 **Or search a topic directly** — type in anything (e.g. `machine learning`, `cricket`, `startups`) and get live results for that exact topic, bypassing the mood system entirely.

Each mood tier maps to a set of possible search categories, defined in a local JSON config file. When a rating is submitted, the app randomly picks one category from the matching tier — so results feel fresh and varied over repeated use.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Backend logic | Python |
| 🔗 Bridge (connects frontend ↔ backend) | Flask |
| 🎨 Frontend | HTML, CSS |
| 🧩 Templating | Jinja2 (built into Flask) |
| 📰 News data | [NewsAPI](https://newsapi.org/) |
| 🗂️ Config | JSON |

**In short:** Python handles all the logic (reading input, picking categories, calling the news API). Flask acts as the bridge that connects that Python logic to the webpage. HTML structures the page, and CSS styles it — together, that's the whole frontend.

---

## ✨ Features

- 🎚️ Mood-to-news mapping via a slider input, based on a configurable range system
- 🔎 Direct topic search as an alternative input path
- 📰 Live article fetching with title, description, source, image, and article link
- 🔀 Randomized category selection within each mood tier for varied results
- 🌑 Clean, dark-themed responsive UI with a sidebar customizer panel and card-based results feed
- 🔐 Environment-based API key management to keep credentials out of source control

---

## 📁 Project Structure

```
Signal10/
├── app.py                 # Flask app: routes, request handling, API calls
├── data.json              # Mood tier ranges and category keywords
├── templates/
│   └── index.html         # Main page template (form + results)
├── requirements.txt       # Python dependencies
├── .env                   # API key (not committed to Git)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup and Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/harshitsanwal/Signal10.git
cd Signal10
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Get a NewsAPI key

Sign up for a free key at [newsapi.org](https://newsapi.org/), then create a `.env` file in the project root:

```
NEWS_API_KEY=your_actual_key_here
```

### 4️⃣ Run the app

```bash
python app.py
```

Then open your browser to:

```
http://127.0.0.1:5000
```

---

## 🗂️ Configuration — `data.json`

Mood tiers, their rating ranges, and their associated search categories are defined here:

```json
{
    "impact_level": {
        "soft_news": {
            "range": [0, 3],
            "keyword": ["entertainment gossip and celebrity news", "feel good human interest stories"]
        },
        "mixed_news": {
            "range": [4, 7],
            "keyword": ["technology trends and gadgets", "business and startup updates"]
        },
        "critical_news": {
            "range": [8, 10],
            "keyword": ["breaking world news", "major political developments"]
        }
    }
}
```

Add, remove, or edit categories and ranges here to customize how ratings map to news types.

---

## 🔐 Security Note

API keys are loaded from a local `.env` file via `python-dotenv` and excluded from version control through `.gitignore`. Never commit `.env` files or hardcode API keys directly into source files.

---

## 📄 License

This project is open for personal and educational use.
