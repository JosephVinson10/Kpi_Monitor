# 📊 KPI Monitor with AI Explanations

This project tracks weekly KPI trends and uses GPT to explain spikes or drops in plain English for executive dashboards.

---

## 🔍 What It Does

- Loads KPI history from CSV (e.g., MRR, Churn, NPS)
- Detects weekly changes in each metric
- Sends metric summary to GPT-3.5 for automated explanation
- Outputs % change and plain-language insight

---

## 🧰 Tech Stack

- Python
- Streamlit
- OpenAI GPT-3.5 Turbo
- Pandas
- `python-dotenv` (for secure API key loading)

---

## 📈 Example KPIs

- MRR (Monthly Recurring Revenue)
- Churn Rate
- Net Promoter Score (NPS)
- Support Ticket Volume

---

## ▶️ How to Run It

1. **Install requirements**

```bash
pip install streamlit openai pandas python-dotenv
Create a .env file in the project root:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key-here
Launch the app

bash
Copy
Edit
streamlit run app.py
📁 Files
app.py — main Streamlit app

kpis.csv — sample KPI input data

prompts/explanation_template.txt — optional external prompt template

.env — holds your OpenAI key (not committed to Git)

🔒 Security Note
Always exclude .env from Git using .gitignore to protect your API key.

gitignore
Copy
Edit
.env
vbnet
Copy
Edit
