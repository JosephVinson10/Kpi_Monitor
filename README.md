# 📊 KPI Monitor with AI Explanations (GPT-4 Turbo)

This project tracks business KPIs and uses **GPT-4 Turbo** to generate high-quality natural-language explanations for performance changes.

---

## 🚀 What It Does

- Loads metrics (e.g., revenue, churn, NPS) from a CSV file
- Compares changes over time
- Uses **GPT-4 Turbo** to generate business-relevant explanations
- Displays all insights in an interactive Streamlit dashboard

---

## 💡 Why GPT-4 Turbo?

We upgraded from GPT-3.5 to **GPT-4 Turbo** for significantly better performance in:

- Context awareness across time-based trends
- Generating more humanlike, executive-level summaries
- Handling nuanced explanations involving multiple metrics

While GPT-4 Turbo has a higher cost per token, its ability to produce smarter, context-rich analysis makes it a worthwhile investment for businesses aiming to automate decision support.

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- OpenAI GPT-4 Turbo
- Dotenv for secure API keys

---

## 📁 Folder Structure

```
kpi_monitor_ai_insights/
├── app.py                          # Streamlit application
├── .env                            # Stores your OpenAI API key
├── data/
│   └── kpis.csv                    # Sample KPI data
├── prompts/
│   └── explanation_template.txt    # Prompt for GPT
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install streamlit openai pandas python-dotenv
```

2. Create your `.env` file:

```
OPENAI_API_KEY=your_openai_key
```

3. Run the dashboard:

```bash
streamlit run app.py
```

---

## 🙌 Author

Built by [Joseph Vinson](https://github.com/JosephVinson10)
